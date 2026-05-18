// NAME: OKURAME DAMIAN EFETOBORE
// DEPAERTMENT: COMPUTER SCIENCE
// MATRIC NUMBER: 250393

// Main class to calculate diode current
public class diode {
	public static void main(String[] args) {
		// Declare and initialize variables for calculation
		double saturationCurrent = 2.0 * (Math.pow(10,-6));
		double charge = 1.602 * (Math.pow(10,-19));
		double kConstant = 1.38 * (Math.pow(10,-23));
		// Initialize temperature array
		double [] temperature = {75,100,125};
		int counter = 0; // Index counter for updating the array
		// Loop to convert all temperatures to kelvin
		for(double Temp : temperature){
			double celsiusTemp = 5*(Temp-32)/9;
			double kelvinTemp = celsiusTemp + 273.15;
			// Replace the temperature in fahrenhait with the converted value in the array
			temperature[counter] = kelvinTemp;
			counter++; 
		// Loop to compute diode current for different temperatures and voltages
		for(double t: temperature){
			for(float V = -1.0f;V<=0.7;V+=0.1){
				double diodeCurrent = saturationCurrent*(Math.exp((charge*V)/(kConstant*t))- 1);
				// Display the calculated diode current for each voltage and temperature value
				System.out.println("The Diode Current at temperature " + t +" kelvin and voltage " + V + " volts is " + diodeCurrent);
			}
		}
		}
		}
	}
