
// ACS575 HW#3  PartI JDBC Programming
// Complete this JDBC program code and show the running .   

import java.sql.*;
import oracle.jdbc.*;
import java.io.*;

public class HW3_PartI_JDBC {
	
	public static void main(String[] args) throws SQLException, IOException {

	    // Prompt the user for connect information
	    System.out.println("Please enter information to connect to a relational DBMS");
	    String user =null;
	    String password =null;
	    String database =null;
      
	    BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
	    
	    System.out.print("user: ");
	    user=buffer.readLine();

	    System.out.print("password: ");
	    password=buffer.readLine();

	    System.out.print("database(e.g., Diamond.pfw.edu:6441:ORCLCDB), localhost:1521:xe : ");
	    database=buffer.readLine();   
	        
	    System.out.print("Connecting to the database...");
	    System.out.flush();
	    System.out.println("Connecting...");
	    
		// (1) Create a database object with username, password and database connection info. 
		Connection conn = 								

		System.out.println("connected. ");

	
		// (2)Create a statement object so we can prepare a static SQL statement
		Statement stmt = 	;				
		
		// (3) Execute a query to list the title of movie which has more than 15 actors.     
		ResultSet rset = 		;			

		System.out.println (">>Movie Title<<");
		
		// (4) // Iterate through the result                                1
		while							// Fill out here
	        System.out.println (     ); // (5) display the movie title.
		
		//(6) Close the stmt statement
						 //Fill out here


		// Prepare to query the ENAME and DEPTNO of employees in a given department from EMP_T table. 
		// (7) Prepare a dinamic SQL query statement to list the information of actors 
		// who presented in a given movie.
		// The query result lists the actor id, actor name, and casting order. 
        // The query result should be sorted by the casting order.
		PreparedStatement pstmt = 								 		
	

	  	//Prompt the user to receive a movie title for the query.
		System.out.println();
	    System.out.println("Please enter a movie title to query its cast (e.g., Aladdin): ");
	    String titleStr =buffer.readLine();
				
		//(8) Set the parameter with the given title.
								//Fill out here 

		//(9) Execute the query statement.  
		rset = 					//Fill out here

		
		System.out.println (">> "+titleStr+" Full Cast <<");
		
		//(10) Iterate through the result  
		while							// Fill out here
			System.out.println (    +","+   +","+   );   //(11) display the cast information, e.g.,  2733, Scott Weinger, 1   
	  
	  	//(12) Close the RseultSet object
							//Fill out here		
		//(13) Close the pstmt statement object
							//Fill out here
		//(14) Close the connection object
							//Fill out here			

    } 
}
