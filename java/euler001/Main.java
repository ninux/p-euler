package euler001;

public class Main {

	public static void main(String[] args) {
	
		int range = 1000;
		int result = 0;

		for(int i = 0; i < range; i++) {
			if (i%3 == 0 || i%5 == 0) {
				result += i;
			}	
		}
		System.out.println(result);
	}

}
