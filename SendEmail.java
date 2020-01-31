// Java program to send email 

import java.util.*; 
import javax.mail.*; 
import javax.mail.internet.*; 
import javax.activation.*; 
import javax.mail.Session; 
import javax.mail.Transport; 


public class SendEmail 
{ 

public static void main(String [] args) 
{	 
	
	String recipient = "gmharshil@gmail.com"; 

	
	String sender = "mounesh97411@gmail.com"; 
 
	String host = "127.0.0.1"; 

	Properties properties = System.getProperties(); 

	properties.setProperty("mail.smtp.host", host); 

	Session session = Session.getDefaultInstance(properties); 

	try
	{ 
		 
		MimeMessage message = new MimeMessage(session); 

		message.setFrom(new InternetAddress(sender)); 
 
		message.addRecipient(Message.RecipientType.TO, new InternetAddress(recipient));

		message.setSubject("This is Suject"); 
 
		message.setText("This is a test mail"); 

		Transport.send(message); 
		System.out.println("Mail successfully sent"); 
	} 
	catch (MessagingException mex) 
	{ 
		mex.printStackTrace(); 
	} 
} 
} 
