Model Architecture planning

Membership
    -slug
    -type (free, pro, enterprise)
    -price
    -stripe plan id

UserMembership
    -user                   (foreignkey to default user)
    -stripe customer id
    -membership type        (foreignkey to Membership)


Subscription
    -user membership        (foreignkey to UserMembership)
    -stripe subcription id
    -active


Course
    -slug
    -title
    -description
    -allowed memberships    (foreignkey to Membership)


Lesson  
    -slug
    -title
    -course                 (foreignkey to Course)
    -position
    -video
    -thumbnail