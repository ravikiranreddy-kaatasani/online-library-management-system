#Ojas online-library-management-system

ABSTRACT : 
Online Library Management System is a system which maintains the information about the books present in the library, their authors, the members of library to whom books are issued, library staff and all. This is very difficult to organize manually. Maintenance of all this information manually is a very complex task. Owing to the advancement of technology, organization of an Online Library becomes much simple. The Online Library Management has been designed to computerize and automate the operations performed over the information about the members, book issues and returns and all other operations. This computerization of library helps in many instances of its maintenances. It reduces the workload of management as most of the manual work done is reduced.

The project aims and objectives that will be achieved after completion of this project are discussed in this subchapter. The aims and objectives are as follows:

 Online book request for issue, return and to extend the date .
 A search column to search availability of books.
 An Admin login page where admin can add books, issue books, take books, calculate fine amount and also update the books.

BACKGROUND OF PROJECT:

E-Library Management System is an application which refers to library systems which are generally small or medium in size. It is used by librarian to manage the library using a computerized system where he/she can add new books, videos and Page sources. Books and student maintenance modules are also included in this system which would keep track of the students using the library and also a detailed description about the books a library contains. With this computerized system there will be no loss of book record or member record which generally happens when a non computerized system is used. All these modules are able to help librarian to manage the library with more convenience and in a more efficient way as compared to library systems which are not computerized.

SYSTEM ANALYSIS:

We will discuss and analyze about the developing process of Library Management System including software requirement specification (SRS) and comparison between existing and proposed system . The functional and non functional requirements are included in SRS part to provide complete description and overview of system requirement before the developing process is carried out. Besides that, existing vs proposed provides a view of how the proposed system will be more efficient than the existing one.

SOFTWARE REQUIREMENT SPECIFICATION

   GENERAL DESCRIPTION PRODUCT DESCRIPTION:

      Library Management System is a computerized system which helps user(librarian) to manage the library daily activity in electronic format. It reduces the risk of paper work such as file lost, file damaged and time consuming.
      It can help user to manage the transaction or record more effectively and timesaving.

   PROBLEM STATEMENT:

      The problem occurred before having computerized system includes:

       File lost:
         When computerized system is not implemented file is always lost because of human environment.Some times due to some human error there may be a loss of records.

       File damaged:
         When a computerized system is not there file is always lost due to some accdent like spilling of water by some member on file accidentally. Besides some natural disaster like floods or fires may also damage the files.
   
       Difficult to search record:
         When there is no computerized system there is always a difficulty in searching of records if the records are large in number .
   
       Space consuming:
         After the number of records become large the space for physical storage of file and records also increases if no computerized system is implemented.

       Cost consuming:
         As there is no computerized system the to add each record paper will be needed which will increase the cost for the management of library.
    
   SYSTEM OBJECTIVES
   
       Improvement in control and performance. 
         The system is developed to cope up with the current issues and problems of library. The system can validate user and is also bug free.
         
       Save cost
         After computerized system is implemented less human force will be requiredxto maintain the library thus reducing the overall cost.
         
       Save time
         Librarian is able to search record by using few clicks of mouse and few search keywords thus saving his valuable time.
         
       Option of online Notice board
         Librarian will be able to provide a detailed description of workshops going in the college as well as in nearby colleges.
         
   SYSTEM REQUIREMENTS
   
      NON FUNCTIONAL REQUIREMENTS:
      
          Product Requirements
         EFFICIENCY REQUIREMENT:
         -----------------------
            When a library management system will be implemented librarian and user will easily acess library as searching and book transaction will be very faster .
         
         RELIABILITY REQUIREMENT:
         ------------------------
            The system should accurately performs member registration ,member validation , report generation, book transaction and search
         USABILITY REQUIREMENT:
         ----------------------
            The system is designed for a user friendly environment so that student and staff of library can perform the various tasks easily and in an effective way.
      
      ORGANIZATIONAL REQUIREMENT:
      ---------------------------
         IMPLEMENTATION REQUIREMNTS:
         ---------------------------
            In implementing whole system it uses html in front end with php as server side scripting language which will be used for database connectivity and the backend ie the database part is developed using mysql.

         DELIVERY REQUIREMENTS:
         ----------------------
            The whole system is expected to be delivered in six months of time with a weekly evaluation by the project guide.

   FUNCTIONAL REQUIREMENTS
   
      1. NORMAL USER
     
         1.1 USER LOGIN
        
            Description of feature:
            -----------------------
               This feature used by the user to login into system. They are required to enter user id and password before they are allowed to enter the system .The user id and password will be verified and if invalid id is there user is allowed to not enter the system. 
               
            Functional requirements:
            -------------------------
               -user id is provided when they register
               -The system must only allow user with valid id and password to enter the system
               -The system performs authorization process which decides what user level can acess to.
               -The user must be able to logout after they finished using system.
               
         1.2 REGISTER NEW USER
        
            Description of feature:
            -----------------------
               This feature can be performed by all users to register new user to create account.
               
            Functional requirements:
            -------------------------
               -System must be able to verify information
               -System must be able to delete information if information is wrong
               
         1.3 REGISTER NEW BOOK:
         
            Description of feature:
            -----------------------
               This feature allows to add new books to the library.
               
            Functional requirements:
            -------------------------
               -System must be able to verify information
               -System must be able to enter number of copies into table.
               - System must be able to not allow two books having same book id.
            
         1.4 SEARCH BOOK:
         
            DESCRIPTION OF FEATURE:
            ------------------------
               This feature is found in book maintenance part . we can search book based on book id , book name , publication or by author name.
               
            Functional requirements:
            ------------------------
               - System must be able to search the database based on select search type
               - System must be able to filter book based on keyword enterd
               - System must be able to show the filtered book in table view
               
            Functional requirements:
            ------------------------
               -System should be able to add detailed information about events .
               -System should be able to display information on notice board available in the homepage of site.      
