import matplotlib.pyplot as plt
import numpy as np

# Ask user what to compare
print("What do you want to compare:")
print("1. Rainfall\n2. Temperature\n3. AQI\n4. Crime Rate(for states)\n5. Demography(religion)\n6. GSDP(for states)")
choice = int(input("Enter number: "))

# If user chooses rainfall (option 1), run this code:
if choice == 1:
    # Replace with real city names and actual rainfall data
    rainfall_data = {
    "amaravati": [4, 5, 10, 17, 42, 104, 155, 179, 136, 142, 37, 10],
    "itanagar": [17, 35, 63, 143, 280, 353, 469, 464, 300, 90, 17, 12],
    "dispur": [11, 21, 40, 141, 259, 356, 377, 345, 227, 73, 11, 6],
    "patna": [13, 17, 8, 7, 44, 154, 346, 298, 219, 59, 10, 6],
    "raipur": [12, 16, 10, 7, 22, 157, 368, 392, 278, 54, 6, 12],
    "panaji": [1, 0, 1, 1, 31, 868, 923, 663, 252, 125, 32, 16],
    "gandhinagar": [0, 0, 1, 1, 6, 129, 332, 238, 104, 23, 4, 1],
    "chandigarh": [23, 33, 27, 13, 23, 109, 265, 288, 156, 20, 6, 7],
    "shimla": [60, 59, 75, 50, 65, 163, 335, 300, 185, 41, 14, 13],
    "dharamshala": [112, 149, 144, 74, 91, 241, 882, 845, 412, 38, 12, 34],
    "ranchi": [13, 16, 14, 10, 33, 186, 360, 328, 254, 55, 7, 4],
    "bengaluru": [3, 4, 10, 25, 75, 88, 108, 124, 195, 186, 59, 15],
    "thiruvananthapuram": [21, 26, 39, 99, 198, 341, 227, 148, 182, 270, 243, 47],
    "bhopal": [10, 9, 5, 6, 18, 115, 360, 338, 196, 61, 13, 6],
    "mumbai": [0.3, 0.1, 0.1, 0.1, 0.3, 523, 799, 585, 327, 89, 16, 3],
    "imphal": [7, 14, 28, 64, 156, 278, 354, 315, 159, 56, 10, 3],
    "shillong": [7, 11, 28, 70, 236, 609, 1082, 633, 353, 61, 9, 5],
    "aizawl": [4, 8, 18, 55, 156, 280, 423, 331, 177, 41, 7, 3],
    "kohima": [10, 15, 33, 89, 180, 265, 446, 318, 220, 50, 10, 4],
    "bhubaneswar": [7, 15, 24, 23, 70, 184, 338, 361, 234, 98, 18, 6],
    "jaipur": [4, 4, 4, 6, 18, 63, 182, 185, 87, 25, 2, 3],
    "gangtok": [18, 22, 37, 117, 347, 527, 572, 503, 429, 133, 21, 3],
    "chennai": [8, 5, 11, 21, 38, 56, 99, 143, 137, 309, 310, 145],
    "hyderabad": [5, 6, 13, 21, 34, 87, 178, 155, 130, 77, 25, 4],
    "agartala": [14, 23, 29, 77, 217, 379, 405, 363, 261, 102, 13, 4],
    "lucknow": [14, 14, 7, 6, 21, 100, 311, 302, 186, 29, 7, 8],
    "dehradun": [53, 60, 56, 22, 37, 231, 535, 474, 269, 28, 7, 19],
    "gairsain": [72, 92, 77, 35, 45, 239, 552, 493, 295, 38, 11, 24],
    "kolkata": [12, 25, 30, 55, 155, 295, 345, 345, 305, 160, 20, 9],
    "port_blair": [29, 20, 19, 60, 180, 470, 678, 573, 417, 253, 239, 83],
    "daman": [0, 0, 1, 2, 13, 353, 645, 566, 295, 60, 7, 2],
    "new_delhi": [20, 20, 15, 13, 30, 80, 185, 235, 130, 14, 5, 9],
    "srinagar": [46, 52, 71, 67, 54, 36, 58, 52, 36, 31, 32, 35],
    "jammu": [60, 66, 54, 31, 35, 107, 307, 267, 151, 18, 15, 21],
    "leh": [3, 2, 2, 4, 10, 9, 17, 16, 6, 4, 3, 2],
    "kavaratti": [11, 1, 2, 11, 100, 401, 268, 159, 176, 115, 182, 78],
    "puducherry": [28, 21, 13, 16, 28, 49, 89, 104, 111, 238, 297, 142]
}

    city1 = input("Enter first capital city (e.g., amaravati): ").strip().lower().replace(" ","_")
    city2 = input("Enter second capital city (e.g., itanagar): ").strip().lower().replace(" ","_")

    if city1 in rainfall_data and city2 in rainfall_data:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        x = np.arange(len(months))
        width = 0.35

        plt.plot(x, rainfall_data[city1], label=city1.capitalize().replace("_"," "), marker='o')
        plt.plot(x, rainfall_data[city2], label=city2.capitalize().replace("_"," "), marker='*')

        plt.xlabel("Month")
        plt.ylabel("Rainfall (mm)")
        plt.title("Monthly Rainfall Comparison")
        plt.xticks(x, months)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()
    else:
        print("One or both cities not found in the rainfall data.")
elif choice==2:
    temperature_data = {
    "Amaravati": [21, 24, 27, 30, 34, 32, 30, 29, 29, 28, 25, 22],
    "Itanagar": [15, 17, 19, 22, 24, 26, 26, 26, 25, 23, 18, 15],
    "Dispur": [16, 18, 22, 25, 27, 29, 29, 29, 28, 26, 21, 17],
    "Patna": [16, 18, 23, 28, 31, 31, 30, 30, 29, 27, 22, 17],
    "Raipur": [20, 23, 27, 31, 34, 31, 29, 28, 28, 28, 24, 20],
    "Panaji": [25, 26, 27, 28, 29, 28, 26, 26, 27, 28, 27, 26],
    "Gandhinagar": [20, 22, 27, 32, 36, 34, 30, 28, 29, 29, 25, 21],
    "Chandigarh": [12, 15, 20, 26, 31, 31, 30, 29, 29, 25, 18, 13],
    "Shimla": [6, 8, 12, 16, 20, 20, 19, 19, 18, 15, 10, 7],
    "Dharamshala": [7, 10, 14, 18, 23, 23, 22, 22, 21, 18, 13, 9],
    "Ranchi": [16, 19, 24, 28, 31, 28, 27, 27, 27, 25, 20, 17],
    "Bengaluru": [21, 22, 24, 26, 25, 24, 23, 23, 23, 23, 22, 21],
    "Thiruvananthapuram": [27, 28, 29, 29, 28, 27, 26, 26, 26, 27, 27, 27],
    "Bhopal": [15, 18, 23, 28, 32, 29, 27, 27, 27, 26, 20, 15],
    "Mumbai": [24, 25, 27, 28, 29, 28, 27, 27, 27, 28, 27, 25],
    "Imphal": [13, 15, 18, 21, 22, 24, 24, 24, 23, 22, 18, 14],
    "Shillong": [9, 12, 15, 17, 19, 19, 19, 19, 19, 17, 13, 9],
    "Aizawl": [12, 15, 18, 20, 22, 23, 22, 22, 22, 21, 16, 12],
    "Kohima": [10, 13, 17, 19, 21, 22, 22, 22, 22, 20, 16, 11],
    "Bhubaneswar": [20, 23, 27, 30, 32, 30, 29, 29, 29, 29, 25, 21],
    "Jaipur": [15, 18, 24, 30, 35, 34, 32, 31, 31, 30, 23, 16],
    "Gangtok": [8, 10, 13, 15, 17, 18, 19, 19, 18, 16, 13, 9],
    "Chennai": [24, 25, 27, 29, 31, 31, 30, 30, 29, 29, 27, 25],
    "Hyderabad": [21, 24, 28, 32, 36, 31, 28, 28, 28, 27, 24, 21],
    "Agartala": [17, 19, 23, 26, 28, 29, 28, 28, 28, 27, 23, 18],
    "Lucknow": [14, 17, 22, 28, 33, 31, 30, 29, 29, 27, 20, 15],
    "Dehradun": [13, 14, 19, 24, 28, 28, 27, 27, 27, 24, 17, 13],
    "Gairsain": [8, 10, 14, 18, 22, 21, 20, 20, 19, 17, 13, 10],
    "Kolkata": [19, 22, 27, 30, 31, 30, 29, 29, 29, 28, 24, 20],
    "Port_blair": [26, 26, 27, 28, 29, 28, 27, 27, 27, 27, 27, 26],
    "Daman": [22, 23, 25, 28, 30, 29, 27, 27, 27, 28, 26, 23],
    "New_delhi": [14, 17, 22, 29, 34, 34, 31, 30, 30, 28, 21, 15],
    "Srinagar": [2, 5, 9, 13, 18, 22, 25, 24, 21, 16, 10, 4],
    "Jammu": [10, 14, 18, 25, 30, 32, 32, 31, 30, 26, 18, 11],
    "Leh": [-2, 0, 5, 10, 14, 17, 20, 18, 14, 8, 2, -2],
    "Kavaratti": [27, 27, 28, 29, 30, 29, 28, 28, 28, 28, 27, 27],
    "Puducherry": [24, 26, 28, 31, 33, 31, 29, 29, 30, 29, 27, 25] } 
  
    city1 = input("Enter first capital city (e.g., amaravati): ").strip().lower().replace(" ","_").capitalize()
    city2 = input("Enter second capital city (e.g., itanagar): ").strip().lower().replace(" ","_").capitalize()
    if city1 in temperature_data and city2 in temperature_data:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        x = np.arange(len(months))
        width = 0.35

        plt.bar(x - width/2, temperature_data[city1], width, label=city1)
        plt.bar(x + width/2, temperature_data[city2], width, label=city2)

        plt.xlabel("Month")
        plt.ylabel("Temperature(degrees))")
        plt.title("Monthly Temperature Comparison")
        plt.xticks(x, months)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("One or both cities not found in the temperature data.")
elif choice==3:
    aqi_data = {
    "Amaravati": [52, 54, 58, 68, 75, 72, 56, 53, 54, 56, 56, 53],
    "Itanagar": [23, 28, 28, 30, 38, 36, 28, 26, 27, 29, 27, 24],
    "Dispur": [60, 55, 60, 85, 95, 80, 65, 64, 63, 60, 56, 55],
    "Patna": [145, 162, 180, 166, 120, 85, 75, 77, 97, 123, 140, 151],
    "Raipur": [110, 98, 106, 124, 133, 106, 88, 77, 78, 85, 92, 105],
    "Panaji": [31, 29, 33, 38, 44, 32, 25, 22, 25, 30, 35, 36],
    "Gandhinagar": [61, 80, 95, 104, 122, 107, 85, 72, 75, 77, 80, 65],
    "Chandigarh": [146, 158, 185, 120, 78, 59, 68, 75, 92, 112, 133, 143],
    "Shimla": [62, 72, 62, 55, 54, 52, 49, 48, 50, 52, 56, 59],
    "Dharamshala": [44, 44, 44, 46, 49, 47, 43, 42, 43, 44, 44, 44],
    "Ranchi": [74, 84, 85, 96, 111, 88, 69, 64, 67, 72, 73, 77],
    "Bengaluru": [47, 46, 49, 54, 64, 52, 44, 40, 39, 41, 45, 49],
    "Thiruvananthapuram": [27, 26, 25, 27, 28, 25, 24, 23, 24, 24, 25, 26],
    "Bhopal": [80, 81, 100, 125, 108, 93, 81, 74, 74, 78, 86, 92],
    "Mumbai": [75, 70, 70, 75, 83, 68, 55, 53, 54, 58, 60, 68],
    "Imphal": [28, 27, 30, 36, 38, 34, 27, 26, 26, 26, 26, 25],
    "Shillong": [22, 23, 24, 29, 30, 27, 23, 22, 22, 22, 22, 21],
    "Aizawl": [14, 13, 13, 13, 12, 13, 13, 12, 12, 11, 11, 12],
    "Kohima": [23, 23, 24, 27, 27, 26, 23, 23, 23, 23, 23, 23],
    "Bhubaneswar": [67, 71, 82, 103, 107, 82, 62, 57, 59, 62, 65, 68],
    "Jaipur": [100, 105, 130, 175, 159, 126, 112, 108, 110, 115, 120, 106],
    "Gangtok": [23, 20, 21, 21, 21, 21, 23, 25, 24, 23, 22, 21],
    "Chennai": [60, 67, 73, 78, 80, 69, 62, 59, 60, 63, 65, 61],
    "Hyderabad": [63, 65, 67, 74, 82, 70, 62, 61, 63, 65, 64, 63],
    "Agartala": [28, 29, 32, 38, 42, 39, 30, 29, 29, 29, 29, 28],
    "Lucknow": [176, 190, 210, 175, 142, 107, 78, 76, 104, 129, 155, 168],
    "Dehradun": [97, 101, 110, 112, 109, 90, 62, 64, 70, 78, 83, 88],
    "Gairsain": [40, 40, 43, 46, 47, 41, 38, 36, 38, 39, 41, 40],
    "Kolkata": [76, 80, 92, 96, 104, 91, 82, 78, 76, 78, 80, 78],
    "Port_blair": [18, 17, 18, 18, 19, 17, 16, 15, 16, 16, 16, 16],
    "Daman": [54, 55, 57, 61, 70, 63, 54, 53, 54, 56, 57, 54],
    "New_delhi": [290, 320, 285, 220, 175, 116, 95, 104, 175, 251, 333, 350],
    "Srinagar": [89, 92, 94, 95, 95, 86, 70, 69, 72, 78, 82, 87],
    "Jammu": [89, 94, 100, 103, 105, 97, 85, 81, 78, 83, 87, 90],
    "Leh": [44, 41, 38, 41, 35, 34, 32, 32, 33, 36, 38, 41],
    "Kavaratti": [21, 20, 18, 19, 19, 18, 17, 17, 17, 18, 18, 20],
    "Puducherry": [22, 23, 23, 23, 24, 23, 21, 21, 22, 22, 22, 22] }
    city1 = input("Enter first capital city (e.g., amaravati): ").strip().lower().replace(" ","_").capitalize()
    city2 = input("Enter second capital city (e.g., itanagar): ").strip().lower().replace(" ","_").capitalize()
    if city1 in aqi_data and city2 in aqi_data:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        x = np.arange(len(months))
        width = 0.35

        plt.bar(x - width/2, aqi_data[city1], width, label=city1)
        plt.bar(x + width/2, aqi_data[city2], width, label=city2)

        plt.xlabel("Month")
        plt.ylabel("AQI")
        plt.title("Monthly AQI Comparison")
        plt.xticks(x, months)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("One or both cities not found in the aqi_data.")
elif choice==4:
    crime_data = {
    "Andhra_pradesh": [3600],
    "Arunachal_pradesh": [5800],
    "Assam": [4400],
    "Bihar": [3100],
    "Chhattisgarh": [4000],
    "Goa": [3800],
    "Gujarat": [2300],
    "Haryana": [3800],
    "Himachal_pradesh": [1800],
    "Jharkhand": [5300],
    "Karnataka": [2700],
    "Kerala": [3500],
    "Madhya_pradesh": [3000],
    "Maharashtra": [3400],
    "Manipur": [2500],
    "Meghalaya": [5100],
    "Mizoram": [900],
    "Nagaland": [1000],
    "Odisha": [3800],
    "Punjab": [2400],
    "Rajasthan": [2500],
    "Sikkim": [1200],
    "Tamil Nadu": [3200],
    "Telangana": [2600],
    "Tripura": [2300],
    "Uttar_pradesh": [7400],
    "Uttarakhand": [1700],
    "West_bengal": [2800],
    "Delhi": [5000],
    "Jammu_and_kashmir": [2200],
    "Ladakh": [1100],
    "Puducherry": [2700],
    "Chandigarh": [3000],
    "Andaman_and_nicobar_islands": [1600],
    "Dadra_and_nagar Haveli":[900],
    "Daman_and_diu": [900],
    "Lakshadweep": [700] }
    state1=input("enter first state:").strip().lower().replace(" ","_").capitalize()
    state2=input("enter second state:").lower().replace(" ","_").capitalize()
    if state1 in crime_data and state2 in crime_data:
        plt.bar(state1,crime_data[state1], label=state1)
        plt.bar(state2,crime_data[state2],label=state2)
        plt.legend()
        plt.xlabel("States")
        plt.ylabel("Crime per 1 lakh people")
        plt.title("Crime Rate Comparision")
        plt.show()
    else:
        print("one or both state not found")
elif choice==5:
    religion_data = {
    "Amaravati": [90.1, 8.3, 1.3, 0.1, 0.1, 0.1, 0.0, 0.0],
    "Itanagar": [29.0, 1.9, 30.3, 0.1, 29.0, 0.1, 9.6, 0.0],
    "Dispur": [61.5, 34.2, 3.7, 0.1, 0.2, 0.1, 0.2, 0.0],
    "Patna": [86.7, 12.3, 0.1, 0.2, 0.2, 0.1, 0.4, 0.0],
    "Raipur": [93.3, 5.2, 0.9, 0.2, 0.2, 0.1, 0.1, 0.0],
    "Panaji": [66.1, 8.3, 25.1, 0.1, 0.1, 0.1, 0.2, 0.0],
    "Gandhinagar": [89.1, 9.7, 0.6, 0.1, 0.1, 0.4, 0.0, 0.0],
    "Chandigarh": [80.8, 4.9, 0.8, 13.1, 0.1, 0.1, 0.1, 0.1],
    "Shimla": [95.6, 2.1, 1.0, 0.1, 0.8, 0.1, 0.2, 0.1],
    "Dharamshala": [54.0, 2.0, 1.0, 0.1, 41.0, 0.1, 1.8, 0.0],
    "Ranchi": [55.0, 14.0, 4.0, 0.1, 0.2, 0.1, 26.5, 0.1],
    "Bengaluru": [78.9, 13.9, 5.0, 1.0, 0.2, 0.5, 0.3, 0.2],
    "Thiruvananthapuram": [66.5, 18.4, 15.0, 0.1, 0.1, 0.1, 0.1, 0.1],
    "Bhopal": [74.2, 22.6, 2.2, 0.1, 0.1, 0.1, 0.1, 0.6],
    "Mumbai": [65.0, 20.6, 13.0, 0.6, 0.2, 0.3, 0.1, 0.2],
    "Imphal": [41.4, 8.3, 46.0, 0.1, 0.1, 0.1, 3.8, 0.2],
    "Shillong": [42.8, 4.5, 46.5, 0.1, 0.1, 0.1, 5.5, 0.4],
    "Aizawl": [2.8, 1.6, 87.2, 0.0, 0.1, 0.0, 8.2, 0.1],
    "Kohima": [8.7, 1.8, 87.9, 0.1, 0.1, 0.1, 1.1, 0.2],
    "Bhubaneswar": [93.6, 5.2, 0.8, 0.1, 0.1, 0.1, 0.1, 0.1],
    "Jaipur": [77.9, 18.6, 0.9, 1.5, 0.1, 0.6, 0.2, 0.2],
    "Gangtok": [57.8, 1.5, 5.0, 0.1, 29.5, 0.1, 5.8, 0.2],
    "Chennai": [80.3, 9.4, 7.7, 0.2, 0.1, 0.3, 1.0, 1.0],
    "Hyderabad": [64.9, 30.1, 2.6, 1.0, 0.1, 0.1, 0.5, 0.7],
    "Agartala": [83.4, 8.6, 3.9, 0.1, 0.1, 0.1, 3.5, 0.3],
    "Lucknow": [76.3, 21.5, 0.4, 1.0, 0.1, 0.2, 0.2, 0.3],
    "Dehradun": [82.3, 11.9, 2.4, 2.0, 0.1, 0.1, 0.4, 0.8],
    "Gairsain": [85.0, 12.0, 1.0, 1.0, 0.1, 0.1, 0.3, 0.5],
    "Kolkata": [70.6, 20.6, 7.5, 0.1, 0.1, 0.1, 0.5, 0.5],
    "Port_blair": [66.0, 9.5, 20.0, 0.1, 0.1, 0.1, 3.5, 0.7],
    "Daman": [93.2, 4.1, 1.0, 0.2, 0.1, 1.1, 0.1, 0.2],
    "New_delhi": [81.7, 12.9, 2.9, 1.5, 0.4, 0.4, 0.1, 0.1],
    "Srinagar": [4.0, 95.0, 0.2, 0.2, 0.1, 0.1, 0.3, 0.1],
    "Jammu": [65.0, 30.0, 0.5, 4.0, 0.1, 0.1, 0.2, 0.1],
    "Leh": [45.0, 15.0, 0.1, 0.1, 39.0, 0.1, 0.5, 0.2],
    "Kavaratti": [3.0, 96.5, 0.2, 0.1, 0.0, 0.0, 0.1, 0.1],
    "Puducherry": [87.3, 6.5, 5.2, 0.1, 0.1, 0.1, 0.4, 0.3] }
    city1 = input("Enter first capital city (e.g., amaravati): ").strip().lower().replace(" ","_").capitalize()
    city2 = input("Enter second capital city (e.g., itanagar): ").strip().lower().replace(" ","_").capitalize()
    if city1 in religion_data and city2 in religion_data:
        plt.subplot(1,2,1)
        plt.pie(religion_data[city1], labels=["Hinduism", "Islam", "Christianity", "Sikhism", "Buddhism", "Jainism","Other","Not Stated"], colors=["orange","green","blue","red","brown","purple","skyblue","pink"], autopct='%1.1f%%', explode=[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])
        plt.title(f"{city1.capitalize()}")
        plt.subplot(1,2,2)
        plt.pie(religion_data[city2], labels=["Hinduism", "Islam", "Christianity", "Sikhism", "Buddhism", "Jainism", "Other","Not Stated"],colors=["orange","green","blue","red","brown","purple","skyblue","pink"], autopct='%1.1f%%', explode=[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])
        plt.title(f"{city2.capitalize()}")
        plt.suptitle("Religion comparision()")
        plt.show()
    else:
        print("one or both cities not in data")
elif choice==6:
    state_gdp_data = {
    "Andhra_pradesh": 13900,
    "Arunachal_pradesh": 420,
    "Assam": 4600,
    "Bihar": 8000,
    "Chhattisgarh": 4300,
    "Goa": 950,
    "Gujarat": 23400,
    "Haryana": 11800,
    "Himachal_pradesh": 2000,
    "Jharkhand": 4300,
    "Karnataka": 22500,
    "Kerala": 10600,
    "Madhya_pradesh": 13200,
    "Maharashtra": 38600,
    "Manipur": 430,
    "Meghalaya": 420,
    "Mizoram": 220,
    "Nagaland": 310,
    "Odisha": 8500,
    "Rajasthan": 14100,
    "Sikkim": 410,
    "Tamil Nadu": 24800,
    "Telangana": 14500,
    "Tripura": 520,
    "Uttar_pradesh": 24500,
    "Uttarakhand": 4600,
    "West_bengal": 17100,
    "Andaman_and_nicobar_islands": 110,
    "Delhi": 11500,
    "Jammua_and_kashmir": 2600,
    "Ladakh": 260,
    "Lakshadweep": 20,
    "Puducherry": 350 }
    state1=input("enter state1:").strip().lower().replace(" ","_").capitalize()
    state2=input("enter state2").strip().lower().replace(" ","_").capitalize()
    if state1 in state_gdp_data and state2 in state_gdp_data:
        plt.bar(state1,state_gdp_data[state1])
        plt.bar(state2,state_gdp_data[state2])
        plt.ylabel("GSDP(in billion INR)")
        plt.title("GSDP comparision")
        plt.show()
    else:
        print("one or both states not in data")





 

    
    
