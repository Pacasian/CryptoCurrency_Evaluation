import requests
import json
from datetime import datetime
import inflect
# Inflect is conversion mechanism from numbers to its convenient word format(alphabetic).
converting = inflect.engine()
# Interacting Section
def calling():
    print("\t\t\t1.Cryptocurrency Details\n\t\t\t2.Cryptocurrency Listing and Ranking\n\t\t\t0.Exit\n")
    print("Enter your Choice")
    choice_section = int(input())
    while(choice_section !=0):
        if choice_section ==1 :
            # The US currency is set as the default currency for this Program.
            currency = "USD"
            print("\t"+"ID"+"\t"+"Currency Name")
            print("\t"+"1:"+"\t"+"British Pound"+"\n"+"\t"+"2:"+"\t"+"Japanese Yen"+"\n"+"\t"+"3:"+"\t"+"Euro"+"\n"+"\t"+"4:"+"\t"+"Indian Rupee"+"\n"+"\t"+"5:"+"\t"+"US Dollar")
            print("Enter the Currency ID, Please")

            choice_currency = int(input())
            # asking the user for Currency Option
            if choice_currency == 1:
                currency = "GBP"
                # Great Britain Pound
            elif choice_currency == 2:
                currency = "JPY"
                # Japanese Yen
            elif choice_currency == 3:
                currency = "EUR"
                # Euro
            elif choice_currency == 4:
                currency = "INR"
                # Indian Rupee
            else:
                currency = "USD"
                 # United States dollar

            print("The Currency of Your choice is "+currency)

            global_url ='https://api.coinmarketcap.com/v2/global/?convert=' + currency

            request = requests.get(global_url)
            results = request.json()
            #print(json.dumps(results, sort_keys=True, indent=4))

            active_currency = results['data']['active_cryptocurrencies']
            active_market = results['data']['active_markets']
            bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
            last_update = results['data']['last_updated']
            global_cap = int(results['data']['quotes'][currency]['total_market_cap'])
            global_volume = int(results["data"]['quotes'][currency]['total_volume_24h'])


            # generating timestamp for the Last_Update
            final_last_update = datetime.fromtimestamp(last_update).strftime('%B %d, %Y at %I:%M%P')

            print("The Number of Active Crypto Currency \t"+str(active_currency))

            # For converting the huge number into words use the Inflect Engine :converting.number_to_words(global_cap))
            print("-> The Last Update was on : "+str(final_last_update))
            print("-> The Global Market Capital : "+str(global_cap)+" "+currency)
            print("-> The Global Bitcoin Volume : "+str(global_volume)+" "+currency)
            # End of the Section 1 , Cryptocurrency Details
            choice_section=6
        elif choice_section == 2:
            listing = ""
            print("currently working on it...")
        elif choice_section == 0:
            print("\t\t\tThank You\n")
            break
        else:
            calling()

calling()
