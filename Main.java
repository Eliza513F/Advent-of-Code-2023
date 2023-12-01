import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int sum = 0; //running sum
		String line = "";
		int firstNum = -1; //-1 = no first num yet
		int lastNum = -1; //just give it a value cuz otherwise the compiler is pissy about it
		String combinedNum = "";
		// loop per line
		for (int i = 0; i < 1000; i++) { //go through every line of input
			
			line = scan.nextLine();
			firstNum = -1;
			line = convertString(line); //convert the word-number string to just having numbers, for Part 2
			
			//loop per character in line
			for (int j = 0; j < line.length(); j++) {
				if (Character.isDigit(line.charAt(j))) {
					// ASCII bullshit requires the -48
					if (firstNum == -1) {
						firstNum = line.charAt(j) - 48;
					}
					lastNum = line.charAt(j) - 48;
				}
			}
			
			combinedNum = String.valueOf(firstNum) + String.valueOf(lastNum);
			
			//System.out.println("CombinedNum = " + combinedNum); //FOR TESTING
			sum += Integer.valueOf(combinedNum);
			System.out.println("sum incremented by " + Integer.valueOf(combinedNum)); //FOR TESTING
			
			//Reset the first num to -1
			firstNum = -1;
		}
		System.out.println(sum); //Output final sum
	}
	
	//converts an input string to one where all the numbers as words are replaced with numbers, for part 2
	static String convertString(String input) {
		System.out.println("Original String: " + input); //Testing
		
		//Ugly af chunk for handling cases such as eightwothree = 823
		//possibilities: oneight, twone, threeight, fiveight, sevenine, eightwo, eighthree, nineight
		if (input.contains("oneight")) {
			input = input.replace("oneight", "18");
		}
		if (input.contains("twone")) {
			input = input.replace("twone", "21");
		}
		if (input.contains("threeight")) {
			input = input.replace("threeight", "38");
		}
		if (input.contains("fiveight")) {
			input = input.replace("fiveight", "58");
		}
		if (input.contains("sevenine")) {
			input = input.replace("sevenine", "79");
		}
		if (input.contains("eightwo")) {
			input = input.replace("eightwo", "82");
		}
		if (input.contains("eighthree")) {
			input = input.replace("eighthree", "83");
		}
		if (input.contains("nineight")) {
			input = input.replace("nineight", "98");
		}
		
		
		if (input.contains("one")) {
			input = input.replace("one", "1");
		}
		if (input.contains("two")) {
			input = input.replace("two", "2");
		}
		if (input.contains("three")) {
			input = input.replace("three", "3");
		}
		if (input.contains("four")) {
			input = input.replace("four", "4");
		}
		if (input.contains("five")) {
			input = input.replace("five", "5");
		}
		if (input.contains("six")) {
			input = input.replace("six", "6");
		}
		if (input.contains("seven")) {
			input = input.replace("seven", "7");
		}
		if (input.contains("eight")) {
			input = input.replace("eight", "8");
		}
		if (input.contains("nine")) {
			input = input.replace("nine", "9");
		}
		System.out.println("Converted to " + input); //Testing
		return input;
	}

}
