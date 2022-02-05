package myjava;

import java.util.Scanner;

public class Myfour {

	public static void main(String[] args) {
		try (// TODO Auto-generated method stub
			Scanner scanner = new Scanner(System.in)) {
	System.out.println("What was the total bill? $");
	 float total_bill = scanner.nextFloat();
	System.out.println("how many people to split the bill? ");
	int bill_split = scanner.nextInt();
	float each_pay =  (total_bill / bill_split);
    System.out.println("each person should pay :" );
	System.out.print(each_pay);					
			}
	}
  
