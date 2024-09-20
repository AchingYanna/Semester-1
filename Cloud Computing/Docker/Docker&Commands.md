<h1><b>DOCKER</b></h1><br>
<img src="https://github.com/user-attachments/assets/e84b0de1-ae3a-4f95-9ab9-c44420d8b327" height = "400", width = "800"><br><br>
Docker is a set of <b>platform as a service (PaaS)</b> products that use OS-level virtualization to deliver software in packages called <b>containers</b>. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.Docker is a tool that is used to automate the deployment of applications in lightweight containers so that applications can work efficiently in different environments in isolation.

<h1><b>Common Commands</b></h1><br><br>
<img src="https://github.com/user-attachments/assets/ac7d5d84-234a-4486-9e16-992ecaad6024" height="400",width="400"><br>
Docker is an open-source project that automates the deployment of applications as movable, independent containers that can run locally or in the cloud. You can divide your applications from your infrastructure with the help of Docker, allowing for quick software delivery and it also allows you to manage your infrastructure in the same ways that you manage your applications. The number of commands found in docker is very huge in number, but we will be looking at the top commands in 

<h3><b>1.Docker Pull command</b></h3><br>

        docker pull <image_name>
This command allows you to pull any image which is present in the official registry of docker, Docker hub. By default, it pulls the latest image, but you can also mention the version of the image.<br>
You can visit here [https://hub.docker.com/search?type=image] and search for the image you want
<br><br>
<img src="https://github.com/user-attachments/assets/deea795b-1a90-46cc-8d5d-1773d541de3c"><br><br>
Here i pulled the image <b>Centos</b>

<h2><b>2. Docker Run command</b></h2>

       docker run <image_name>

This command is used to run a container from an image. The docker run command is a combination of the docker create and docker start commands. It creates a new container from the image specified and starts that container.       
<br>
<img src="https://github.com/user-attachments/assets/12ed5e0e-9834-41e2-99f6-77869a95ea67">
<br><br>
Here i executed the run command on the <b>Centos</b> image. The <b>Sleep 20</b> here tells the container that it should run for only 20 seconds before shutting down. Generally it can be in the form

      docker run <image_name> sleep <n>

Where "n" is the number of seconds you want the container to run     

<h2><b>3. Docker ps</b></h2>
This command (by default) shows us a list of all the running containers. We can use various flags with it.

  *  <h3><b>-a</b> flag</h3><br><br>
       Shows us all the containers, stopped or running.<br>
       <img src ="https://github.com/user-attachments/assets/aac8db90-1cf5-454b-8851-9db2def0c48f"><br><br>
       Here the command shows the two containers stopped.
 *   <h3><b>--l flag:</b></h3>
       Shows us the latest container.

 *  <h3><b>-q flag:</b></h3><br><br>
       Shows us only the ID of the containers  
       <img src="https://github.com/user-attachments/assets/4ba1cb77-43d6-4680-81ea-9d26825d0827">


<h3><b>4. Docker Stop</b></h3>

      docker stop <container_ID>
This command allows you to stop a container if it has crashed or you want to switch to another one<br><br>
<img src="https://github.com/user-attachments/assets/efccb4a6-7433-4e6b-b314-fd20e1f1fa0a">

<h3><b>5. Docker Start</b></h3>
       docker start <container_ID>

  Suppose you want to start the stopped container again, you can do it with the help of this command.<br><br>
  <img src="https://github.com/user-attachments/assets/9f75d7ff-6a6b-4468-9c50-71804e086c43"><br>
  A syou can see that the container had been exited before but usingthe <b>Start</b> command you can restart the container

<h3><b>6. Docker rm</b></h3>

        docker rm <container_name or ID>
To delete a container. By default when a container is created, it gets an ID as well as an imaginary name such as confident_boyd, heuristic_villani, etc.
<br><br>
<img src="https://github.com/user-attachments/assets/ab27304e-eb21-4615-9e32-7d81ce917454"><br><br>
<img src="https://github.com/user-attachments/assets/4a2bcb08-ede3-46b2-a6d9-e499d3817ac0">
<br><br>
You can see that an already stopped container is still listen, however you can use the <b>rm</b> command to remove it

<h3><b>7. Docker Images</b></h3>

      docker images
  This command will show you all the images stored locally<br><br>
  <img src="https://github.com/user-attachments/assets/419c0133-88cd-4ad2-a66e-12c7393866fc">


<h3><b>8. Docker RMI</b></h3>

      docker rmi <Image Id or Image name>

Just like the Rm command this command will remove the images
<br><br>
<img src="https://github.com/user-attachments/assets/52b0fa08-2cce-414e-9f56-fd9d8f68121c"><br><br>
<img src="https://github.com/user-attachments/assets/e2259cb2-59a6-41bf-acfb-5c6d596334df"><br><br>
As you can see the image "Ubuntu" is now removed


  

       

       
      
