package easy_problems.from_1_to_50;

import java.sql.*;
import java.util.*;
import java.util.function.Consumer;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
class Employee {
    private String name;

    public Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    private int age;

}


interface EmployeeFunction {
    String run(Employee e);
}

public class Hello {


    public static void main(String[] args) {


       new Thread(() -> {
           System.out.println("Printing from the Runnable");
           System.out.println("Line 2");
       }).start();


       Employee ivan = new Employee("ivan", 33);
       Employee israel = new Employee("israel", 39);
       Employee ramses = new Employee("ramses", 49);


        List<Employee> employees = new ArrayList<Employee>();
        employees.add(ivan);
        employees.add(israel);
        employees.add(ramses);


        Collections.sort(employees, (Employee employee1, Employee employee2) ->
                employee1.getName().compareTo(employee2.getName()));

        employees.forEach((employee) -> {
            System.out.println(employee.getName());
        });

        System.out.println("This is another and better compacted way of using lambdas in java");


        Consumer<Employee> myLambda = (employee) -> {
            System.out.println(employee.getName());
        };

        employees.forEach(myLambda);

        EmployeeFunction employeeNames = (e) -> e.getName();

        EmployeeFunction format = (e) -> e.getName();

        String result = format.run(ivan);
        System.out.println("This is the amazing result of the lambda function: " + result);









        try (Connection connection = DriverManager.getConnection("jdbc:postgresql://localhost:5432/testing", "postgres", "1234")) {

            System.out.println("Java JDBC PostgreSQL Example");

            System.out.println("Connected to PostgreSQL database!");

            if (connection!=null){
                System.out.println("Connection OK");
            }
            else {
                System.out.println("There was an error");
            }

            String query = "SELECT * FROM t1";

            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()){
                System.out.println(rs.getString("id") + " " + rs.getString("name"));
            }


        } /*catch (ClassNotFoundException e) {
            System.out.println("PostgreSQL JDBC driver not found.");
            e.printStackTrace();
        }*/ catch (SQLException e) {
            System.out.println("Connection failure.");
            e.printStackTrace();
        }


    }


}
