## Gym Management

A gym management system is a software application designed to help gym owners and managers streamline their operations and manage day-to-day tasks. This may include things like membership management, scheduling, billing and payments, facility and equipment management, and reporting and analytics.

#Update Bump Version
##Major Version Bump
##Patch Version Bump
##Release Added



## Change

##### Push Again

#### License
MIT


#### Version Dependancy
ERPNext: v14.23.0 (version-14)
Frappe Framework: v14.34.0 (version-14)
Gym Management: v0.0.1

#### Role Created
Gym Admin
Gym Trainer
Gym Member


#### Role Profile Created
Gym Trainer

Gym Member

#### Module Profile Created

Gym Admin Module Profile -- Only access Gym Managemment amd Core Modules

Gym Trainer Module Profile-- Only access Gym Managemment

Gym Member Module Profile-- Only access Gym Managemment

####  How to Install

bench get-app https://github.com/jaydeep-sigzen/gymmgt.git

bench --site *site_name* install-app gymmgt

bench --site *site_name* migrate

#### Steps
1> Create one Gynm Admin user from Administrator user with select Gym Admin Role AND  Gym Admin Module Profile.

2> Set Password for the Gym Admin

3> Login with Gym Admin User

![Screenshot from 2023-05-02 13-21-05](https://user-images.githubusercontent.com/127377825/235610187-bd01dabf-612c-45be-8621-f9220fbbb83f.png)

4> Now Gym Admin have all access for the Gym Managment.

Note - After successfully add Gym Member Or Gym Trainer we have to manualu create user by click Create button on top of created user details.



