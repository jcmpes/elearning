This is really simple eLearning platform built with Python and Django.

Users can create an account.

The default membership is Free.

There are Amateur and Pro memberships users can subscribe to.

My application connects with Stripe API everytime a user is created and creates a customer in my Stripe account.

Once logged in, users can browse courses and lessons.

When they hit a course that is not included in the Free membership they are prompted to upgrade their membership.

Users can use their credit card to proceed with payment.

Payment is processed by Stripe.

When payment is complete the subscription type is updated and the user can access the course.

Staff members can create courses in the admin page.

Lessons containing a video and a description can be also created.

The app courses contains the models, views and templates to create and visualize courses and lessons. And the logic to show subscribed users certain content depending on their current subscription. 

The app memberships contains the logic and views to manage the subsciptions of users to the different membership types. Also here is all the logic needed to connect with Stripe and create and update subscriptions not only on my app but on Stripe too.

Finally, the app register holds the logic for creating and authenticating users using crispy forms and the Django authentication system.