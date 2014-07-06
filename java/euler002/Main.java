package euler002;

public class Main {

	public static void main(String[] args){
	
		int limit = 4000000;

		int a = 1;
		int b = 1;

		int swp = 0;

		int sum = 0;

		while (swp < limit) {
			swp = a+b;
			a = b;
			b = swp;
			if (swp%2 == 0) {
				sum += swp;
			}
		}

		System.out.println("Result: " + sum);

	}

}
