package easy_problems.from_1_to_50;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;

public class JDBC {
    public static void main(String[] args) throws Exception{

        //Registering the Driver
        DriverManager.registerDriver(new com.mysql.jdbc.Driver());
        //Getting the connection
        String mysqlUrl = "jdbc:mysql://157.253.236.116:8080/WWImportersTransactional";
        Connection con = DriverManager.getConnection(mysqlUrl, "Estudiante_41", "5RQM0M7SCG");
        System.out.println("Connection established......");
        //Retrieving the meta data object
        DatabaseMetaData metaData = con.getMetaData();
        String[] types = {"TABLE"};
        //Retrieving the columns in the database
        ResultSet tables = metaData.getTables(null, null, "%", types);
        while (tables.next()) {
            System.out.println(tables.getString("TABLE_NAME"));
        }

    }
}
