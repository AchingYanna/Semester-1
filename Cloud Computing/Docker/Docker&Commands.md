<h1><b>DOCKER</b></h1><br>
<img src="https://github.com/user-attachments/assets/b8007547-9d36-47f7-9450-0a42bdc9abae" height = "400", width = "800"><br><br>
Docker is a set of <b>platform as a service (PaaS)</b> products that use OS-level virtualization to deliver software in packages called <b>containers</b>. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.Docker is a tool that is used to automate the deployment of applications in lightweight containers so that applications can work efficiently in different environments in isolation.

<h1><b>Common Commands</b></h1><br><br>
<img src="https://github.com/user-attachments/assets/4db13d19-6237-479a-9b95-c03eb2000a6f" height="400",width="400"><br>
Docker is an open-source project that automates the deployment of applications as movable, independent containers that can run locally or in the cloud. You can divide your applications from your infrastructure with the help of Docker, allowing for quick software delivery and it also allows you to manage your infrastructure in the same ways that you manage your applications. The number of commands found in docker is very huge in number, but we will be looking at the top commands in 

<h3><b>1.Docker Pull command</b></h3><br>

        docker pull <image_name>
This command allows you to pull any image which is present in the official registry of docker, Docker hub. By default, it pulls the latest image, but you can also mention the version of the image.<br>
You can visit here [https://hub.docker.com/search?type=image] and search for the image you want
<br><br>
<img src="https://github.com/user-attachments/assets/d70e0066-9d65-4724-a663-85218f77eaf5"><br><br>
Here i pulled the image <b>Centos</b>

<h2><b>2. Docker Run command</b></h2>

       docker run <image_name>

This command is used to run a container from an image. The docker run command is a combination of the docker create and docker start commands. It creates a new container from the image specified and starts that container.       
<br>
<img src="https://github.com/user-attachments/assets/5780e40d-3b3c-4080-af69-e22d3127c03c">
<br><br>
Here i executed the run command on the <b>Centos</b> image. The <b>Sleep 20</b> here tells the container that it should run for only 20 seconds before shutting down. Generally it can be in the form

      docker run <image_name> sleep <n>

Where "n" is the number of seconds you want the container to run     

<h2><b>3. Docker ps</b></h2>
This command (by default) shows us a list of all the running containers. We can use various flags with it.

  *  <h3><b>-a</b> flag</h3><br><br>
       Shows us all the containers, stopped or running.<br>
       <img src ="https://github.com/user-attachments/assets/f8ff9e4e-34c4-4f87-9fca-b17982f3a9e1"><br><br>
       Here the command shows the two containers stopped.
 *   <h3><b>--l flag:</b></h3>
       Shows us the latest container.

 *  <h3><b>-q flag:</b></h3><br><br>
       Shows us only the ID of the containers  
       <img src="https://github.com/user-attachments/assets/f848e4a7-3fa6-45da-8bbc-488be8ca8604">


<h3><b>4. Docker Stop</b></h3>

      docker stop <container_ID>
This command allows you to stop a container if it has crashed or you want to switch to another one<br><br>
<img src="https://github.com/user-attachments/assets/b64ceab0-08d7-47fa-92df-bbfb11035679">

<h3><b>5. Docker Start</b></h3>
       
       docker start <container_ID>

  Suppose you want to start the stopped container again, you can do it with the help of this command.<br><br>
  <img src="https://github.com/user-attachments/assets/298e0791-cfa3-4689-a1e9-237c200a5610"><br>
  As you can see that the container had been exited before but usingthe <b>Start</b> command you can restart the container

<h3><b>6. Docker rm</b></h3>

        docker rm <container_name or ID>
To delete a container. By default when a container is created, it gets an ID as well as an imaginary name such as confident_boyd, heuristic_villani, etc.
<br><br>
<img src="https://github.com/user-attachments/assets/91405b10-5ce1-4d52-9509-2e4d7675c748"><br><br>
<img src="https://github.com/user-attachments/assets/16ef629d-7f8b-4414-afec-da8326023071">
<br><br>
You can see that an already stopped container is still listen, however you can use the <b>rm</b> command to remove it

<h3><b>7. Docker Images</b></h3>

      docker images
  This command will show you all the images stored locally<br><br>
  <img src="https://github.com/user-attachments/assets/6fdb09b3-58f0-4bef-b86e-e18a5a6d96eb">


<h3><b>8. Docker RMI</b></h3>

      docker rmi <Image Id or Image name>

Just like the Rm command this command will remove the images
<br><br>
<img src="https://github.com/user-attachments/assets/f077506e-c421-427c-a9ba-62e8f7737d36"><br><br>
<img src="https://github.com/user-attachments/assets/c4965348-bb5d-4ef1-a4de-de8fe07b74d0"><br><br>
As you can see the image "Ubuntu" is now removed


  

       

       
      
