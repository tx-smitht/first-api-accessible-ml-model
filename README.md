# first-api-accessible-ml-model
INTEX HACK!!! 
This code is my first attempt at making a machine learning model accesible through an API. I followed this tutorial to deploy the API https://dev.to/nick_langat/how-to-deploy-a-fastapi-app-to-aws-ec2-server-46d4 
This might be the route that my group and I go for intex to incorporate machine learning models into our web app. I thought it could be useful to some folks. 

Check out the "app.py" file to see how the actual model (the model.pkl) is opened, read, and used by the api. 
By the end, you should be able to use postman as shown and it'll spit back a prediction!

How I would go about replicating what I did:
1. Look at the "ML_Part.py" file. It is included to explain how the "model.pkl" file came into existence. I actually created the pkl file in Google Colab (using the code in "ML_Part.py"), then downloaded it (the pkl) to my machine then uploaded it to this github repository (but in theory (I think) you could have all the python code in the "ML_Part.py" be in the "app.py" and you could end up with the same final result).
2. Make the model.pkl using Colab
3. Follow the tutorial that I followed. I slightly modified the app.py shown in the tutorial so that instead of having just a "home" route, it would have a "/predict" route, so you'll need to use mine to make the api work.

Hopefully that helps and isn't too confusing! Good luck!

![Screenshot ](https://user-images.githubusercontent.com/112910116/230518135-dc1cd4cb-67e2-4416-9e93-143bb2e24118.jpg)


Checklist:
- When doing the tutorial, make sure you read everything, not just the screenshots. It is pretty unclear sometimes. When you get started with an EC2, you'll have to install virtualenv onto it. (sudo pip3 install virtualenv or something, look it up). Then create an env and use it to install the dependancies (like the tutorial says)

- Every time you stop or start your ec2 instance, make sure that the ip in sudo nano /etc/nginx/sites-enabled/api is correct. 

- Look into the files that you create using nano. They have paths in them that need to be right or else it wont work. For example, if you have "venv" instead of "env", your paths will be off and not work. Check them to make sure they are right.

- Then make sure that you do sudo service gunicorn start, sudo systemctl start gunicorn.socket, sudo systemctl enable gunicorn.socket, sudo systemctl daemon-reload, sudo systemctl restart gunicorn , sudo systemctl restart nginx

- sudo systemctl status gunicorn.service can be used to see if gunicorn is running
- ps aux | grep gunicorn needs to return 4 or 5 lines with gunicorn workers for it to be working. Otherwise, if it only returns one line, you have something wrong.
