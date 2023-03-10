#!/usr/bin/env python3
from flts import vuelo_nonstop, vuelo_1stop, vuelo_con_escala, vuelo_3stop, vuelo_tbs, vuelo_longest, firefox, vuelo_pap, vuelo_exp_uk, vuelo_cortito
import re

from datetime import datetime, date, timedelta

#main variable. Update to test
VUELO = vuelo_3stop#vuelo_3stop#vuelo_con_escala#vuelo_tbs#vuelo_3stop ###CHANGE THIS VALUE

class sell_this_flight(object):

    #//Regex selectors!
    flight = "flight\n.+\d"
    cos = "\([a-zA-Z]\)"
    date2 = "\(...\)\n\nA.*"#'Arrives.*[A-Z][a-z][a-z][ ]\d+'
    date1 = '•.*[A-Z][a-z][a-z][ ]\d+'
    airports = "[A-Z][A-Z][A-Z](?=\))"
    re_departure = "Departure\d+:\d+[a-z]+"
    re_arrival = "Arrival\d+:\d+[a-z]+"
    layovers = "Layover.*"
    
    IATA_airlines = {
        "ABX Air":'GB',
        "Aegean Airlines":'A3',
        "Aer Lingus":'EI',
        "Aero Republica":'P5',
        "Aeroflot":'SU',
        "Aerolineas Argentinas":'AR',
        "Aeromar":'VW',
        "Aeromexico":'AM',
        "Africa World Airlines":'AW',
        "Air Algérie":'AH',
        "Air Arabia":'G9',
        "Air Astana":'KC',
        "Air Austral":'UU',
        "Air Baltic":'BT',
        "Air Botswana":'BP',
        "Air Burkina":'2J',
        "Air Cairo":'SM',
        "Air Caledonie":'TY',
        "Air Canada":'AC',
        "Air Caraibes":'TX',
        "Air China":'CA',
        "Air Corsica":'XK',
        "Air Dolomiti":'EN',
        "Air Europa":'UX',
        "Air France":'AF',
        "Air Guilin":'GT',
        "Air India":'AI',
        "Air Koryo":'JS',
        "Air Macau":'NX',
        "Air Madagascar":'MD',
        "Air Malta":'KM',
        "Air Mauritius":'MK',
        "Air Moldova":'9U',
        "Air New Zealand":'NZ',
        "Air Niugini":'PX',
        "Air Nostrum":'YW',
        "Air Peace":'P4',
        "Air Serbia":'JU',
        "Air Seychelles":'HM',
        "Air Tahiti":'VT',
        "Air Tahiti Nui":'TN',
        "Air Tanzania":'TC',
        "Air Transat":'TS',
        "Air Vanuatu":'NF',
        "AirBridgeCargo Airlines":'RU',
        "Aircalin":'SB',
        "Airlink":'4Z',
        "Alaska Airlines":'AS',
        "Albastar":'AP',
        "Allied Air":'4W',
        "AlMasria Universal Airlines":'UJ',
        "American Airlines":'AA',
        "ANA":'NH',
        "APG Airlines":'GP',
        "Arkia Israeli Airlines":'IZ',
        "Asiana Airlines":'OZ',
        "ASKY":'KP',
        "ASL Airlines France":'5O',
        "Atlantic Airways":'RC',
        "Atlas Air":'5Y',
        "Austrian Airlines":'OS',
        "Avianca":'AV',
        "Avianca Costa Rica":'LR',
        "Avianca Ecuador":'2K',
        "Azerbaijan Airlines":'J2',
        "Azores Airlines":'S4',
        "Azul Brazilian Airlines":'AD',
        "Badr Airlines":'J4',
        "Bahamasair":'UP',
        "Bamboo Airways":'QH',
        "Bangkok Airways":'PG',
        "Batik Air":'ID',
        "Batik Air Malaysia":'OD',
        "Biman Bangladesh Airlines":'BG',
        "Binter Canarias":'NT',
        "Blue Air":'0B',
        "BoA Boliviana de Aviacion":'OB',
        "Braathens Regional Airways":'TF',
        "British Airways":'BA',
        "Brussels Airlines":'SN',
        "Bulgaria Air":'FB',
        "Camair-Co":'QC',
        "Cambodia Angkor Air":'K6',
        "Capital Airlines":'JD',
        "Cargojet Airways":'W8',
        "Cargolux":'CV',
        "Caribbean Airlines":'BW',
        "Carpatair":'V3',
        "Cathay Pacific":'CX',
        "Cebu Pacific":'5J',
        "Challenge Airlines":'5C',
        "China Airlines":'CI',
        "China Cargo Airlines":'CK',
        "China Eastern":'MU',
        "China Express Airlines":'G5',
        "China Postal Airlines":'CF',
        "China Southern Airlines":'CZ',
        "CityJet":'WX',
        "Condor":'DE',
        "Congo Airways":'8Z',
        "Copa":'CM',
        "Corendon Airlines":'XC',
        "Corsair International":'SS',
        "Croatia Airlines":'OU',
        "Cubana":'CU',
        "Cyprus Airways":'CY',
        "Czech Airlines":'OK',
        "Delta Air Lines":'DL',
        "Delta":'DL',
        "DHL Air":'D0',
        "DHL Aviation":'ES',
        "Eastern Airlines":'2D',
        "Eastern Airways":'T3',
        "Egyptair":'MS',
        "EL AL":'LY',
        "Emirates":'EK',
        "Ethiopian Airlines":'ET',
        "Etihad Airways":'EY',
        "EuroAtlantic Airways":'YU',
        "European Air Transport":'QY',
        "Eurowings":'EW',
        "EVA Air":'BR',
        "Evelop Airlines":'E9',
        "FedEx Express":'FX',
        "Fiji Airways":'FJ',
        "Finnair":'AY',
        "Fly Baghdad":'IF',
        "flydubai":'FZ',
        "FlyEgypt":'FT',
        "Flynas":'XY',
        "FLYONE":'5F',
        "French Bee":'BF',
        "Fuzhou Airlines":'FU',
        "Garuda Indonesia":'GA',
        "Georgian Airways":'A9',
        "German Airways":'ZQ',
        "GOL Linhas Aereas":'G3',
        "Gulf Air":'GF',
        "GX Airlines":'GX',
        "Hahn Air":'HR',
        "Hainan Airlines":'HU',
        "Hawaiian Airlines":'HA',
        "Hebei Airlines":'NS',
        "Hong Kong Air Cargo":'RH',
        "Hong Kong Airlines":'HX',
        "Hong Kong Express Airways":'UO',
        "IBERIA":'IB',
        "Icelandair":'FI',
        "IndiGo":'6E',
        "Iran Air":'IR',
        "Iran Airtour Airline":'B9',
        "Iran Aseman Airlines":'EP',
        "Israir":'6H',
        "ITA Airways":'AZ',
        "Japan Airlines":'JL',
        "Japan Transocean Air":'NU',
        "Jazeera Airways":'J9',
        "Jeju Air":'7C',
        "JetBlue Airways":'B6',
        "Jin Air":'LJ',
        "Jordan Aviation":'R5',
        "Juneyao Airlines":'HO',
        "Kam Air":'RQ',
        "Kenya Airways":'KQ',
        "KLM":'KL',
        "Korean Air":'KE',
        "Kunming Airlines":'KY',
        "Kuwait Airways":'KU',
        "La Compagnie":'B0',
        "LAM":'TM',
        "Lao Airlines":'QV',
        "LATAM Airlines Brasil":'JJ',
        "LATAM Airlines Colombia":'4C',
        "LATAM Airlines Ecuador":'XL',
        "LATAM Airlines Group":'LA',
        "LATAM Airlines Paraguay":'PZ',
        "LATAM Airlines Peru":'LP',
        "LATAM Cargo Brasil":'M3',
        "LATAM Cargo Chile":'UC',
        "Loong Air":'GJ',
        "LOT Polish Airlines":'LO',
        "Lucky Air":'8L',
        "Lufthansa":'LH',
        "Lufthansa Cargo":'LH',
        "Lufthansa CityLine":'CL',
        "Luxair":'LG',
        "Malaysia Airlines":'MH',
        "Mandarin Airlines":'AE',
        "Martinair Cargo":'MP',
        "MasAir":'M7',
        "Mauritania Airlines International":'L6',
        "MEA":'ME',
        "MIAT Mongolian Airlines":'OM',
        "MNG Airlines":'MB',
        "Myanmar Airways International":'8M',
        "National Airlines":'N8',
        "NCA Nippon Cargo Airlines":'KZ',
        "Neos":'NO',
        "Nesma Airlines":'NE',
        "Nile Air":'NP',
        "NordStar":'Y7',
        "Nordwind Airlines":'N4',
        "Nouvelair":'BJ',
        "Okay Airways":'BK',
        "Olympic Air":'OA',
        "Oman Air":'WY',
        "Paranair":'ZP',
        "Pegas Fly":'EO',
        "Pegasus Airlines":'PC',
        "PGA-Portugalia Airlines":'NI',
        "Philippine Airlines":'PR',
        "PIA Pakistan International Airlines":'PK',
        "Polar Air Cargo":'PO',
        "Poste Air Cargo":'M4',
        "Precision Air":'PW',
        "Privilege Style":'P6',
        "Qantas":'QF',
        "Qatar Airways":'QR',
        "Ravn Alaska":'7H',
        "Rossiya Airlines":'FV',
        "Royal Air Maroc":'AT',
        "Royal Brunei":'BI',
        "Royal Jordanian":'RJ',
        "Ruili Airlines":'DR',
        "RusLine":'7R',
        "RwandAir":'WB',
        "S7 Airlines":'S7',
        "Safair":'FA',
        "SAS":'SK',
        "SATA Air Acores":'SP',
        "Saudi Arabian Airlines":'SV',
        "SCAT Airlines":'DV',
        "SF Airlines":'O3',
        "Shandong Airlines":'SC',
        "Shanghai Airlines":'FM',
        "Shenzhen Airlines":'ZH',
        "Sichuan Airlines":'3U',
        "Silk Way West Airlines":'7L',
        "Singapore Airlines":'SQ',
        "SKY Airline":'H2',
        "Smartavia":'5N',
        "Smartwings":'QS',
        "Solomon Airlines":'IE',
        "Somon Air":'SZ',
        "South African Airways":'SA',
        "SpiceJet":'SG',
        "SriLankan Airlines":'UL',
        "SunExpress":'XQ',
        "Suparna Airlines":'Y8',
        "SWISS":'LX',
        "Syrianair":'RB',
        "T way Air":'TW',
        "TAAG Angola Airlines":'DT',
        "TACA":'TA',
        "TAP Portugal":'TP',
        "TAROM":'RO',
        "Tassili Airlines":'SF',
        "Thai Airways International":'TG',
        "Thai Lion Air":'SL',
        "Thai Smile":'WE',
        "Tianjin Airlines":'GS',
        "TUIfly":'X3',
        "Tunisair":'TU',
        "Turkish Airlines":'TK',
        "Ukraine International Airlines":'PS',
        "UNI AIR":'B7',
        "United Airlines":'UA',
        "United":'UA',
        "UPS Airlines":'5X',
        "Ural Airlines":'U6',
        "Urumqi Air":'UQ',
        "UTair":'UT',
        "Uzbekistan Airways":'HY',
        "Vietjet":'VJ',
        "Vietnam Airlines":'VN',
        "Virgin Atlantic":'VS',
        "Virgin Australia":'VA',
        "Vistara":'UK',
        "Volaris":'Y4',
        "Volotea":'V7',
        "Vueling":'VY',
        "Wamos Air":'EB',
        "West Air":'PN',
        "WestJet":'WS',
        "White coloured by you":'WI',
        "Wideroe":'WF',
        "World2Fly":'2W',
        "Xiamen Airlines":'MF',
        "YTO Cargo Airlines":'YG',
        "Swiss International Air Lines":'LX',
        "TACA Airlines":'TA'
    }



    def __init__(self, schedule):
    #//Each raw component!
        self._flight = re.findall(self.flight, schedule)
        self._cos = re.findall(self.cos, schedule)
        #self._date2 = re.findall(self.date2, schedule)
        self._date2 = [re.findall('[A-Z][A-Z][A-Z]', x)[0] for x in re.findall(self.date2, schedule)]
        self._date1 = re.findall(self.date1, schedule)
        self._cities = re.findall(self.airports, schedule)
        self._departure = re.findall(self.re_departure, schedule)#[0].strip("Arrival")
        self._arrival = re.findall(self.re_arrival, schedule)#[0].strip("Arrival")
        self._layovers = re.findall(self.layovers, schedule)
        self._day1 = re.findall('[A-Z][a-z][a-z] \d+', self._date1[0])[0] #print (day1) #Jan 4
        


    def containsPM(self, time12h_raw):
        try:
            time12_full = re.findall("\d+...[p][m]",time12h_raw)[0]
            time12_hour_old = re.findall('\d+(?=\:)', time12h_raw)[0]
            #Don't add 12 if 12:00pm!!!!
            time12_hour_new = f"{int(time12_hour_old)+12}"
            novo = time12_full.replace(time12_hour_old, time12_hour_new)
            return "".join(re.findall("\d+", novo)).zfill(4)
        except IndexError: return("".join(re.findall("\d+", time12h_raw)).zfill(4))
        except:
            raise


    def validMCT(self, str_num1, str_num2):
        return (int(str_num1)-int(str_num2))<0


    def check_MCT(self, str_num1, str_num2):
        return self.validMCT(self.containsPM(str_num1), self.containsPM(str_num2))


    def ordered_flights(self):
        ###return [x.strip('flight\n') for x in self._flight]
        _all_airlines = [x.strip('flight\n') for x in self._flight]
        _len = len(_all_airlines)
        re_airline = '[^0-9]+'
        re_number  = '[0-9]+'

        #return [self.IATA_airlines[re.findall(re_airline, _all_airlines[0])[0].strip()] for x in range(_len)] #Oneliner! ;D

        _decoded = []
        for x in range(_len):
            try:
                _1st_bit = self.IATA_airlines[re.findall(re_airline, _all_airlines[x])[0].strip()] #AA, UA, AS, DL, etc.
                _2nd_bit = re.findall(re_number, _all_airlines[x])[0] # 4684, 681, 2, 56, etc
                _decoded.append(f"{_1st_bit} {_2nd_bit}") #AA 4684, UA 681, AS 2, DL 56, etc.
            except KeyError:
                _decoded.append(_all_airlines[x])
        return _decoded




        #print(re.findall(re_airline, _all_airlines[0]))
        #self.IATA_airlines[_all_airlines[0]])


    def ordered_cos(self):
        return [x.strip("()") for x in self._cos]


    def ordered_citypairs(self):
        return [f"{self._cities[i]}{self._cities[i+1]}" for i in range(0, len(self._cities), 2)]


    #def elpepe(self): return ':v'


    def ordered_dates(self):
        today = 0
        tomorrow = 0
        more=[self.check_MCT(self._arrival[i], self._departure[i+1]) for i in range(0, len(self._arrival)-1, 2)] #added a "-1"

        for x in more:
            if x == True:
                today += 1

        day1 = re.findall('[A-Z][a-z][a-z] \d+', self._date1[0])[0] #print (day1) #Jan 4
        day1_EX = datetime.strptime(day1, '%b %d') #print(day1_EX) #1900-01-04 00:00:00

        for x in self._date2: tomorrow+=1

        deff = []
        #print(today, tomorrow)

        deff.append(day1_EX)
        for x in range(today):
            deff.append(day1_EX)

        if tomorrow > 0:
            for x in range(tomorrow):
                deff.append(day1_EX + timedelta(days=1))



        "12Jan 12Jan 13Jan"


        final = []
        for x in deff:
            final.append(x.strftime('%d%b').zfill(5))

        final.sort()
        return final


    def ordered_dates(self):

        """
            TODO: add shit here, idk xD
        """

        first, arrivals,  layovers, cities, nextday_departures = self._day1, self._arrival, self._layovers, self._cities, self._date2

        additional_dates = []

        nodupe = [] #each city appears a single time
        for x in cities:
            if x not in nodupe:
                nodupe.append(x)


        for x in nodupe:

            #puts a +1 on every index at which a day-change occurs #[0, 1, 0]
            if x in nextday_departures:
                additional_dates.append(1)
            else:
                additional_dates.append(0)
        
        additional_dates.pop(0)

        

        initial = datetime.strptime(f"{first}{datetime.now().year}", '%b %d%Y')
        _arrivals = [datetime.strftime(datetime.strptime(re.findall("\d+:\d+am|\d+:\d+pm", x)[0],"%I:%M%p"), "%H:%M") for x  in arrivals] #['09:30', '13:10'] from ['Arrival9:30am', 'Arrival1:10pm']


        definitive = []
        posterior = [] #departure date of each following flight

        definitive.append(datetime.strftime(initial, '%d%b'))


        AH= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
        AM= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

        try:
            LH = [re.findall('\d+', x)[0] for x in layovers]
            LM = [re.findall('\d+', x)[1] for x in layovers]
        except IndexError:
            LH = ['0'] 
            LM = [re.findall('\d+', x)[0] for x in layovers]


        print(LH, LM)

        for i, val in enumerate(layovers): #limit is set by number of connections
            posterior.append(datetime.strftime(initial + timedelta(days=int(additional_dates[i])) + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%d%b')) #=Sum of date, arrival & connection time
            initial = datetime.strptime(posterior[i], '%d%b') #Next iteration's "initial" is updated

        #posterior.sort() #I think it's useless here...
        
        definitive.extend(posterior)
        return definitive



    def result(self):

        _long_sell_format = []
        for i, val in enumerate(self.ordered_cos()):
            _long_sell_format.append(f"ss {self.ordered_flights()[i]} {self.ordered_cos()[i]} {self.ordered_dates()[i]} {self.ordered_citypairs()[i]} 1")

        _final_string = "\n".join(_long_sell_format)

        return(_final_string)

        













            



if __name__=="__main__":
    # sold2nd = sell_this_flight(vuelo_longest)
    # print(sold2nd.result())
    # print(sold2nd.ordered_flights())
    # print(sold2nd.ordered_cos())
    # print(sold2nd.ordered_citypairs())
    # print(sold2nd.ordered_dates())

    #sold3rd = sell_this_flight(vuelo_con_escala)
    #print(sold3rd.ordered_dates())
    #print(sold3rd.result())
    # print(sold3rd.ordered_flights())
    # print(sold3rd.ordered_cos())
    # print(sold3rd.ordered_citypairs())
    # print(sold3rd.ordered_dates())
    # print(sold3rd._arrival)
    # print(sold3rd._departure)
    #print(sold3rd.result())
    #print(sold3rd.ordered_dates())

    vc = sell_this_flight(vuelo_cortito)
    print(vc.result())
    #print(vc.ordered_dates())

    osogei = sell_this_flight("""
    San Salvador to New York
    5:40am - 2:59pm (8h 19m, 1 stop)5:40am through 2:59pm (8h 19m, 1 stop)

    American Airlines • Tue, Mar 21
    Departure5:40am - San Salvador
    El Salvador Intl. (SAL)

    3h 39m flight
    American Airlines 1408
    Boeing 737-800WiFi, entertainment and power on this flight
    Economy/Coach (N)
    Arrival10:19am - Miami
    Miami Intl. (MIA)

    Layover: 1h 40m in Miami
    Departure11:59am - Miami
    Miami Intl. (MIA)

    3h flight
    American Airlines 1479
    Boeing 737 MAX 8WiFi, entertainment and power on this flight
    Economy/Coach (N)
    Arrival2:59pm - New York
    John F. Kennedy Intl. (JFK)

    Hide details
        """)
    
    print(osogei.result())

    outlier = sell_this_flight("""
    Los Angeles to Tampa
    8:00am - 5:13pm (6h 13m, 1 stop)8:00am through 5:13pm (6h 13m, 1 stop)

    American Airlines • Tue, Mar 21
    Departure8:00am - Los Angeles
    Los Angeles Intl. (LAX)

    3h 1m flight
    American Airlines 2459
    Airbus A321WiFi, entertainment and power on this flight
    Economy/Coach (V)
    Arrival1:01pm - Dallas
    Dallas-Fort Worth Intl. (DFW)

    Layover: 54m in Dallas
    Departure1:55pm - Dallas
    Dallas-Fort Worth Intl. (DFW)

    2h 18m flight
    American Airlines 898
    Airbus A321WiFi, entertainment and power on this flight
    Economy/Coach (V)
    Arrival5:13pm - Tampa
    Tampa Intl. (TPA)

    Hide details
        """)

    print(outlier.result())


    # _test2 = sell_this_flight(vuelo_3stop)
    # print(_test2.result())
    # print(_test2.ordered_flights())
    # print(_test2.ordered_cos())
    # print(_test2.ordered_citypairs())
    # print(_test2.ordered_dates()) #should be ['12Jan', '12Jan', '12Jan']

    #_test_1=sell_this_flight(firefox) #fails because it displays flight as "flightAmerican Airlines" and this makes regex fail
    #print(_test_1.result())
    # print(_test_1.ordered_flights())
    # print(_test_1.ordered_cos())
    # print(_test_1.ordered_citypairs())
    # print(_test_1.ordered_dates())

    #_test_2=sell_this_flight(vuelo_pap)
    #print(_test_2.result())
    # print(_test_2.ordered_flights())
    # print(_test_2.ordered_cos())
    # print(_test_2.ordered_citypairs())
    # print(_test_2.ordered_dates())

    #_test_3=sell_this_flight(vuelo_exp_uk)
    #print(_test_2.result())
    # print(_test_3.ordered_flights())
    # print(_test_3.ordered_cos())
    # print(_test_3.ordered_citypairs())
    #print(_test_3.ordered_dates())


    # _test1 = sell_this_flight(vuelo_con_escala)
    # print(_test1.ordered_flights())
    # print(_test1.ordered_cos())
    # print(_test1.ordered_citypairs())
    # print(_test1.ordered_dates())


['Aeromexico 477', 'Aeromexico 628']
['V', 'V']
['IAHMEX', 'MEXSAL']
['12Jan', '12Jan']




# from datetime import datetime, date, timedelta
# print(date.today().strftime('%d%b')) #--27Dec
# print(datetime.strptime('27Dec22','%d%b%y')) #--2022-12-27 00:00:00
# print(datetime.strptime('27Dec','%d%b')) #--1900-12-27 00:00:00
