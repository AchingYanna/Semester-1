# Tutorial: Launching a VPC Using the AWS Management Console

This guide will walk you through creating and configuring a Virtual Private Cloud (VPC) using the AWS Management Console.

<h2>1. Accessing the VPC Dashboard</h2>
<ol>
  <li><b>Log in</b> to the <a href="https://aws.amazon.com/console/">AWS Management Console</a>.</li>
  <li><b>Navigate to the VPC Dashboard</b> by typing "VPC" in the search bar and selecting <b>VPC</b>.</li>
</ol>

<h2>2. Creating a VPC</h2>
<ol>
  <li><b>Click on "Create VPC"</b> on the VPC Dashboard.</li>
  <li>
    <b>Enter the following configuration:</b>
    <ul>
      <li><b>Name tag</b>: Specify a name for the VPC (e.g., <code>MyFirstVPC</code>).</li>
      <li><b>IPv4 CIDR block</b>: Input a CIDR block (e.g., <code>10.0.0.0/16</code>).</li>
      <li><b>IPv6 CIDR block</b>: Select <b>No IPv6 CIDR block</b> or configure one as needed.</li>
      <li><b>Tenancy</b>: Choose between <b>Default</b> or <b>Dedicated</b>.</li>
    </ul>
  </li>
  <li><b>Click "Create VPC"</b> to finalize the creation.</li>
</ol>

<h2>3. Configuring Subnets</h2>
<ol>
  <li><b>Navigate to the "Subnets" section</b> within the VPC Dashboard.</li>
  <li><b>Click "Create Subnet"</b> and provide the following details:</li>
  <ul>
    <li><b>VPC</b>: Select the VPC created earlier.</li>
    <li><b>Name tag</b>: Assign a name to the subnet.</li>
    <li><b>Availability Zone</b>: Choose an appropriate zone (e.g., <code>us-west-1a</code>).</li>
    <li><b>CIDR block</b>: Enter a subnet range (e.g., <code>10.0.1.0/24</code>).</li>
  </ul>
  <li><b>Click "Create Subnet"</b> to save the configuration.</li>
</ol>

<h2>4. Creating an Internet Gateway (IGW)</h2>
<ol>
  <li><b>Navigate to "Internet Gateways"</b> on the left-hand menu.</li>
  <li><b>Click "Create Internet Gateway"</b> and provide a name.</li>
  <li><b>Click "Create"</b> and then attach the IGW to your VPC:</li>
  <ul>
    <li>Select the IGW.</li>
    <li>Click <b>Actions > Attach to VPC</b>.</li>
    <li>Select your VPC and confirm.</li>
  </ul>
</ol>

<h2>5. Configuring Route Tables</h2>
<ol>
  <li><b>Navigate to "Route Tables"</b> in the sidebar.</li>
  <li><b>Click "Create route table"</b> and associate it with your VPC.</li>
  <li><b>Add a route:</b></li>
  <ul>
    <li>Select the route table and click <b>Edit routes</b>.</li>
    <li>Click <b>Add route</b> and set <code>0.0.0.0/0</code> as the destination.</li>
    <li>Select the Internet Gateway as the target.</li>
    <li>Save the changes.</li>
  </ul>
  <li><b>Associate the route table with a subnet:</b></li>
  <ul>
    <li>Click <b>Subnet associations</b>.</li>
    <li>Select <b>Edit subnet associations</b> and choose the subnet you created.</li>
    <li>Save your changes.</li>
  </ul>
</ol>

<h2>6. Configuring Security Groups</h2>
<ol>
  <li><b>Navigate to "Security Groups"</b> in the sidebar.</li>
  <li><b>Create a security group</b> and associate it with your VPC.</li>
  <li>
    <b>Set inbound rules:</b>
    <ul>
      <li>Add rules to allow necessary traffic (e.g., <b>HTTP (80)</b>, <b>SSH (22)</b>).</li>
    </ul>
  </li>
  <li><b>Set outbound rules:</b> Outbound traffic is typically set to allow all by default.</li>
  <li><b>Save</b> the security group configuration.</li>
</ol>

<h2>7. Launching an EC2 Instance in Your VPC</h2>
<ol>
  <li><b>Navigate to the "EC2 Dashboard"</b> and click <b>Launch Instance</b>.</li>
  <li><b>Choose an Amazon Machine Image (AMI)</b>.</li>
  <li><b>Select an instance type</b> based on your needs.</li>
  <li>
    <b>Configure the instance:</b>
    <ul>
      <li><b>Network</b>: Choose your VPC.</li>
      <li><b>Subnet</b>: Select the public subnet.</li>
      <li><b>Auto-assign Public IP</b>: Enable for internet connectivity.</li>
    </ul>
  </li>
  <li><b>Add storage</b> and <b>tags</b> as needed.</li>
  <li><b>Select or create a security group</b> configured earlier.</li>
  <li><b>Review</b> and <b>Launch</b> the instance.</li>
</ol>

# Tutorial: Adding Load Balancers to Your VPC and Simulating Load Balancing

This guide explains how to set up a load balancer in your VPC and test its functionality by simulating a failure.

<h2>1. Adding an Application Load Balancer (ALB) to Your VPC</h2>
<ol>
  <li><b>Navigate to the "EC2 Dashboard"</b> in the AWS Management Console.</li>
  <li><b>Select "Load Balancers"</b> from the sidebar and click <b>Create Load Balancer</b>.</li>
  <li><b>Choose "Application Load Balancer"</b>.</li>
  <li>
    <b>Configure basic settings:</b>
    <ul>
      <li><b>Name</b>: Provide a name for the load balancer (e.g., <code>MyALB</code>).</li>
      <li><b>Scheme</b>: Select <b>Internet-facing</b> or <b>Internal</b>, depending on your needs.</li>
      <li><b>IP address type</b>: Choose <b>IPv4</b> or <b>Dualstack</b> for IPv4/IPv6.</li>
    </ul>
  </li>
  <li>
    <b>Configure network mapping:</b>
    <ul>
      <li>Select your VPC.</li>
      <li>Choose the subnets in which the load balancer will be available (ensure these subnets are public).</li>
    </ul>
  </li>
  <li><b>Configure security groups</b>:
    <ul>
      <li>Select or create a security group that allows HTTP/HTTPS traffic.</li>
    </ul>
  </li>
  <li>
    <b>Configure the listener:</b>
    <ul>
      <li>Choose HTTP (port 80) or HTTPS (port 443) as the protocol.</li>
      <li>Ensure that a default action is set to forward traffic to a target group.</li>
    </ul>
  </li>
  <li><b>Click "Create Load Balancer"</b>.</li>
</ol>

<h2>2. Creating a Target Group</h2>
<ol>
  <li><b>Navigate to "Target Groups"</b> in the sidebar.</li>
  <li><b>Click "Create target group"</b> and provide the following details:</li>
  <ul>
    <li><b>Target type</b>: Select <b>Instances</b> or <b>IP addresses</b>.</li>
    <li><b>VPC</b>: Choose your VPC.</li>
    <li><b>Port</b>: Specify the port for traffic (e.g., port 80).</li>
  </ul>
  <li><b>Click "Next"</b> and register targets:</li>
  <ul>
    <li>Select the instances you want to include in the target group.</li>
    <li>Click <b>Add to registered</b> and then <b>Create target group</b>.</li>
  </ul>
</ol>

<h2>3. Testing Load Balancing by Simulating Failure</h2>
<ol>
  <li><b>Access your load balancer's DNS name</b> from the "Load Balancers" page.</li>
  <li><b>Verify traffic distribution</b>:
    <ul>
      <li>Open a web browser and navigate to the DNS name.</li>
      <li>Ensure that the load balancer is properly distributing traffic between your instances.</li>
    </ul>
  </li>
  <li>
    <b>Simulate a failure:</b>
    <ul>
      <li>Stop or terminate one of the instances registered in the target group.</li>
      <li>Observe the load balancer redirecting traffic to the healthy instance(s).</li>
    </ul>
  </li>
  <li>
    <b>Check the "Target Groups" health status</b>:
    <ul>
      <li>Go to "Target Groups" and click on the target group name.</li>
      <li>Monitor the health status of the instances.</li>
    </ul>
  </li>
</ol>

