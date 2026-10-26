import csv, random, datetime as dt, math, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
random.seed(42)
airports=[("YUL","Montréal–Trudeau","Montréal","QC","Canada","North America","HUB"),("YYZ","Toronto Pearson","Toronto","ON","Canada","North America","HUB"),("YVR","Vancouver Intl","Vancouver","BC","Canada","North America","HUB"),("YYC","Calgary Intl","Calgary","AB","Canada","North America","HUB"),("YOW","Ottawa Macdonald-Cartier","Ottawa","ON","Canada","North America","DOMESTIC"),("YHZ","Halifax Stanfield","Halifax","NS","Canada","North America","DOMESTIC"),("YEG","Edmonton Intl","Edmonton","AB","Canada","North America","DOMESTIC"),("YWG","Winnipeg Richardson","Winnipeg","MB","Canada","North America","DOMESTIC"),("YQB","Québec City Jean Lesage","Québec","QC","Canada","North America","DOMESTIC"),("JFK","New York JFK","New York","NY","USA","North America","INTERNATIONAL"),("LAX","Los Angeles Intl","Los Angeles","CA","USA","North America","INTERNATIONAL"),("ORD","Chicago O'Hare","Chicago","IL","USA","North America","INTERNATIONAL"),("MIA","Miami Intl","Miami","FL","USA","North America","INTERNATIONAL"),("CUN","Cancún Intl","Cancún","QR","Mexico","North America","SUN"),("LHR","London Heathrow","London","ENG","United Kingdom","Europe","INTERNATIONAL"),("CDG","Paris Charles de Gaulle","Paris","IDF","France","Europe","INTERNATIONAL"),("FRA","Frankfurt","Frankfurt","HE","Germany","Europe","INTERNATIONAL"),("NRT","Tokyo Narita","Tokyo","CHB","Japan","Asia","INTERNATIONAL"),("HND","Tokyo Haneda","Tokyo","TYO","Japan","Asia","INTERNATIONAL"),("GRU","São Paulo Guarulhos","São Paulo","SP","Brazil","South America","INTERNATIONAL")]
w=csv.writer(open("DIM_AIRPORT.csv","w",newline=""));w.writerow(["AIRPORT_CODE","AIRPORT_NAME","CITY","PROVINCE_STATE","COUNTRY","REGION","AIRPORT_TYPE"]);w.writerows(airports)
codes=[a[0] for a in airports];hubs=["YUL","YYZ","YVR","YYC"]
routes=[]
for h in hubs:
  for c in codes:
    if c!=h and (c not in hubs or h<c): routes.append((h,c))
fleet={"A220-300":137,"A321":190,"B737 MAX 8":169,"B787-9":298,"B777-300ER":400,"A330-300":297}
def ac(o,d):
  intl=[a for a in airports if a[0]==d][0][6]=="INTERNATIONAL" and [a for a in airports if a[0]==d][0][5]!="North America"
  return random.choice(["B787-9","B777-300ER","A330-300"]) if intl else random.choice(["A220-300","A321","B737 MAX 8"])
start,end=dt.date(2025,1,1),dt.date(2026,10,31)
fl=[];fid=0;num={}
for i,r in enumerate(routes): num[r]="AC"+str(100+i*7)
d=start
while d<=end:
  season=1+0.25*math.sin((d.timetuple().tm_yday-100)/365*2*math.pi)+(0.15 if d.weekday() in (4,6) else 0)
  growth=1.08 if d.year==2026 else 1.0
  n=int(round(random.gauss(14*season*growth,1.5)))
  for r in random.sample(routes,min(n,len(routes))):
    o,de=r if random.random()<.5 else (r[1],r[0])
    fid+=1;a=ac(o,de);hr=random.randint(6,22)
    delay=max(0,int(random.expovariate(1/18)) if random.random()<.3 else 0)
    if d.month in (12,1,2) and random.random()<.15: delay+=random.randint(20,120)
    st="CANCELLED" if random.random()<.015 else ("DELAYED" if delay>15 else "ON_TIME")
    if st=="CANCELLED": delay=0
    dist=random.randint(500,1500) if a in ("A220-300","A321","B737 MAX 8") else random.randint(5000,11000)
    fl.append([fid,num[r]+("" if o==r[0] else "1"),d.isoformat(),o,de,f"{hr:02d}:{random.choice(['00','15','30','45'])}",a,fleet[a],dist,delay,st])
  d+=dt.timedelta(1)
w=csv.writer(open("DIM_FLIGHT.csv","w",newline=""));w.writerow(["FLIGHT_ID","FLIGHT_NUMBER","FLIGHT_DATE","ORIGIN_AIRPORT_CODE","DESTINATION_AIRPORT_CODE","SCHEDULED_DEPARTURE_TIME","AIRCRAFT_TYPE","SEAT_CAPACITY","DISTANCE_KM","DEPARTURE_DELAY_MINUTES","FLIGHT_STATUS"]);w.writerows(fl)
fn="Émilie Olivier Sophie Liam Chloé Noah Maya Lucas Zoé William Ava Félix Léa Ethan Amélie Jacob Priya Arjun Mei Wei Sarah David Fatima Omar Isabelle Mathieu Hannah Ryan Julie Marc".split()
ln="Tremblay Gagnon Roy Côté Bouchard Gauthier Morin Lavoie Fortin Smith Brown Wilson Martin Lee Patel Singh Nguyen Chen Wong MacDonald Leblanc Pelletier Kim Garcia Dubois Campbell".split()
tiers=["NONE"]*45+["25K"]*20+["35K"]*15+["50K"]*10+["75K"]*6+["SUPER ELITE"]*4
pax=[]
for p in range(1,3001):
  f,l=random.choice(fn),random.choice(ln)
  pax.append([p,f,l,f"{f.lower()}.{l.lower()}{p}@example.com".encode('ascii','ignore').decode(),random.choice(["Canada"]*7+["USA","France","United Kingdom","Japan"]),random.choice(hubs+["YOW","YHZ","YEG"]),random.choice(tiers),dt.date(random.randint(1950,2006),random.randint(1,12),random.randint(1,28)).isoformat(),(dt.date(2015,1,1)+dt.timedelta(random.randint(0,3800))).isoformat()])
w=csv.writer(open("DIM_PASSENGER.csv","w",newline=""));w.writerow(["PASSENGER_ID","FIRST_NAME","LAST_NAME","EMAIL","COUNTRY","HOME_AIRPORT_CODE","AEROPLAN_TIER","DATE_OF_BIRTH","MEMBER_SINCE"]);w.writerows(pax)
bk=[];bid=0
cabins=[("ECONOMY",.78,1),("PREMIUM_ECONOMY",.12,1.8),("BUSINESS",.10,4.5)]
for f in fl:
  k=random.randint(1,4) if f[10]=="CANCELLED" else random.randint(3,8)
  fdate=dt.date.fromisoformat(f[2])
  for _ in range(k):
    bid+=1;c=random.choices(cabins,weights=[x[1] for x in cabins])[0]
    base=(0.18*f[8]+90)*c[2]*random.uniform(.7,1.4)
    lead=int(random.expovariate(1/40))+1
    ch=random.choices(["WEB","MOBILE_APP","TRAVEL_AGENT","CALL_CENTER"],[45,30,20,5])[0]
    status="CANCELLED" if f[10]=="CANCELLED" else random.choices(["FLOWN","NO_SHOW","REFUNDED"],[93,4,3])[0]
    if fdate>dt.date(2026,10,23) and status!="CANCELLED": status="CONFIRMED"
    fare=round(base,2);tax=round(fare*.15+35,2)
    bk.append([bid,f"PNR{bid:06d}",f[0],random.randint(1,3000),(fdate-dt.timedelta(lead)).isoformat(),c[0],ch,random.randint(1,2) if random.random()<.15 else 1,fare,tax,round(fare+tax,2),int(f[8]*(1 if c[0]=="ECONOMY" else 1.5)),status])
# Business-class propensity rises with Aeroplan tier (separate RNG keeps the rest of the data stable)
r2=random.Random(7);tier_of={p[0]:p[6] for p in pax}
biz={"NONE":.06,"25K":.09,"35K":.13,"50K":.20,"75K":.30,"SUPER ELITE":.45}
mult={c[0]:c[2] for c in cabins}
for b in bk:
  pb=biz[tier_of[b[3]]];u=r2.random()
  new="BUSINESS" if u<pb else ("PREMIUM_ECONOMY" if u<pb+.12 else "ECONOMY")
  if new!=b[5]:
    b[8]=round(b[8]/mult[b[5]]*mult[new],2);b[9]=round(b[8]*.15+35,2);b[10]=round(b[8]+b[9],2)
    b[11]=int(b[11]/(1 if b[5]=="ECONOMY" else 1.5)*(1 if new=="ECONOMY" else 1.5));b[5]=new
w=csv.writer(open("FACT_BOOKING.csv","w",newline=""));w.writerow(["BOOKING_ID","BOOKING_REFERENCE","FLIGHT_ID","PASSENGER_ID","BOOKING_DATE","CABIN_CLASS","BOOKING_CHANNEL","SEATS_BOOKED","BASE_FARE_CAD","TAXES_FEES_CAD","TOTAL_FARE_CAD","AEROPLAN_POINTS_EARNED","BOOKING_STATUS"]);w.writerows(bk)
print(len(airports),len(fl),len(pax),len(bk))
