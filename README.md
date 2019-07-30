# CourseSniper

A simple webapp that enables students to monitor (and automatically register) for classes they are interested in. During my time at the University of Rochester getting into popular classes was difficult. The provided waitlist functionality did not work as expected, so CourseSniper was developed a solution to monitor classes people cared about. We used a python backend to monitor the course registration site and an AngularJS webapp to take requests from users. The backend would track changes in the registration site and alert users of course opennings. Automatic registration functionality was tested, but that required providing your personal username and password.

## Sample

```
Delivered-To: rpillai3@u.rochester.edu

From: UR Course Alert <ur.coursesniper@gmail.com>
To: rpillai3@u.rochester.edu
Subject: Course 50367 has openned!
Message-ID: <1a47cdc1-6243-6322-cc3f-6c673152f067@gmail.com>
X-Mailer: nodemailer (2.6.0; +http://nodemailer.com/;
 SMTP/2.7.2[client:2.12.0])
Date: Tue, 06 Sep 2016 22:39:57 +0000
MIME-Version: 1.0

Content-Type: text/plain
Content-Transfer-Encoding: 7bit

Course 50367 has openned!

Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

The class CSC 254 is open PROGRAMMING LANGUAGE DESIGN & IMPLEMENTATION for Fall 2016
```
