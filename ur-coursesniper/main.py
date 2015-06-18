#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


MAIN_PAGE_HTML = """\
<head lang="en">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Snipes your courses for University of Rochester">
    <meta name="author" content="Matthew Lee">
    <meta name="keywords" content="course, sniper, coursesniper, rochester, university,schedule,classes,">

    <!-- Bootstrap CSS -->
    <link href="static/assets/css/bootstrap.css" rel="stylesheet">
<!--    <link href="assets/css/jumbotron-narrow.css" rel="stylesheet"> -->

    <link href="static/assets/css/cover.css" rel="stylesheet">

    <!-- Custom styles -->
    <link href="static/assets/css/main.css" rel="stylesheet">


    <meta charset="UTF-8">
    <title>UR Course Sniper</title>
</head>

<body>
<!--
    <div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" class="active"><a href="#">Sniper</a></li>
            <li role="presentation"><a href="#">About</a></li>
            <li role="presentation"><a href="#">FAQ</a></li>
          </ul>
        </nav>
        <h3>University of Rochester CourseSniper</h3>
      </div>

        <form action="/" method="post" id = "infor">
            <div class="form-group">
                <label for="CRN">Enter CRN here</label>
                    <input type="text" class="form-control" id="CRN" placeholder="Enter unique CRN for the section you want, Ex: '10901'">
            </div>
            <div class="form-group">
                <label for="emaili">Password</label>
                <input type="email" class="form-control" id="emaili" placeholder="exampleaddress@gmail.com">
            </div>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Snipe it!</button>
        </form>

      <div class="jumbotron">
        <h1>Jumbotron heading</h1>
        <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
      </div>
         <div class="mastfoot">
            <div class="inner">
              <p>Created by Matthew Lee and Raayan Pillai.</p>
            </div>
          </div> -->


    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <h3 class="masthead-brand">University of Rochester Course Sniper</h3>
              <nav>
                <ul class="nav masthead-nav">
                  <li class="active"><a href="#">Sniper</a></li>
                  <li><a href="#">About</a></li>
                  <li><a href="#">FAQ</a></li>
                </ul>
              </nav>
            </div>
          </div>
        <div class="basicinfo">
        <h1 class="basicinfo">We track courses for you.</h1>
        <p class="lead">Simply just enter your email and the CRN for your course section and and we'll notify you when it opens up.</p>

          </div>
        <form action="/" method="post" id = "infor">
            <div class="form-group">
                <label for="CRN">Enter CRN here</label>
                <input type="text" name="CRNbox" class="form-control" id="CRN" placeholder="Enter unique CRN for the section you want, Ex: '10901'">
            </div>
            <div class="form-group">
                <label for="emaili">Email</label>
                <input type="email" name="emailbox" class="form-control" id="emaili" placeholder="exampleaddress@gmail.com">
            </div>
            <button class="btn btn-lg btn-default" type="submit">Snipe it!</button>
        </form>




          <div class="mastfoot">
            <div class="inner">
              <p>Created by Matthew Lee and Raayan Pillai.</p>
            </div>
          </div>

        </div>

      </div>

    </div>


</body>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

    def post(self):
        crn = self.request.get('CRNbox')
        email = self.request.get('emailbox')
        ##Enter code for post on mongoDB here
        self.response.write('Successfully submitted a follow request for CRN: ')
        self.response.write(crn)
        self.response.write(' with the email: ')
        self.response.write(email)
        self.response.write('<p> </p>')
        self.response.write('Have a nice day!')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
