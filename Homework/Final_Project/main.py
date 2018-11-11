#!/usr/bin/env python
import os
import jinja2
import webapp2
import logging
import random
import uuid

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")


class AboutUsHandler(BaseHandler):
    def get(self):
        return self.render_template("aboutus.html")


TOKENDICT = {}


class ContactHandler(BaseHandler):

    def get(self):
        global TOKENDICT

        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        token = str(uuid.uuid4())

        TOKENDICT[token] = number_1 + number_2
        logging.debug("Loaded Contact Page")
        return self.render_template("contact.html", params={"n1": number_1,
                                                            "n2": number_2,
                                                            "token": token})

    def post(self):
        global TOKENDICT

        logging.info("Received POST Request {}".format(self.request.POST))
        email = self.request.get("email")
        persons = self.request.get("persons")
        reasons = self.request.get("reasons")
        comment = self.request.get("comment")
        robotest = self.request.get("robotest")
        token = self.request.get("token")

        is_human = TOKENDICT[token] == int(robotest.strip())
        del TOKENDICT[token]
        return self.response.out.write(
            "email: {}, persons: {}, reasons: {}, comment: {}, is_human: {}"
                .format(email, persons, reasons, comment, is_human)
        )


class NewsletterHandler(BaseHandler):
    def get(self):
        return self.render_template("newsletter.html")

    def post(self):
        logging.info("Received POST Request {}".format(self.request.POST))
        mail = self.request.get("mail")
        gridRadios = self.request.get("gridRadios")
        checkbox = self.request.get("checkbox")

        return self.response.out.write("mail: {}, gridRadios: {}, checkbox: {}".format(mail, gridRadios, checkbox))


class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")


class SecretHandler(BaseHandler):
    def get(self):
        return self.render_template("secretnumber.html")

    def post(self):
        logging.info("Received POST Request {}".format(self.request.POST))
        secret = 48
        guess = int(self.request.get("guess"))

        result = None

        if secret == guess:
            result = "You're great, the answer is correct. The secret number is 48."
        elif secret > guess:
            result = "Your guess is too low. Try again!"
        elif secret < guess:
            result = "Your guess is too high. Try again!"

        params = {"result": result}

        return self.render_template("secretresult.html", params=params)


class ConversionHandler(BaseHandler):
    def get(self):
        return self.render_template("converter.html")

    def post(self):
        first_num = float(self.request.get("quantity"))
        selected_unit = self.request.get("unit")

        second_num = None
        second_unit = None

        if selected_unit == "miles":
            second_num = first_num * 1.60934
            second_unit = "kilometers"
        elif selected_unit == "km":
            second_num = first_num * 0.621371
            second_unit = "miles"

        params = {"first_num": first_num, "first_unit": selected_unit, "second_num": second_num,
                  "second_unit": second_unit}

        return self.render_template("finalconversion.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/aboutus', AboutUsHandler),
    webapp2.Route('/contact', ContactHandler),
    webapp2.Route('/newsletter', NewsletterHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/secretnumber', SecretHandler),
    webapp2.Route('/converter', ConversionHandler),
], debug=True)