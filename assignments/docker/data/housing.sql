--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.9
-- Dumped by pg_dump version 9.5.9

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: buy; Type: TABLE; Schema: public;
--

CREATE TABLE buy (
    neighborhood text,
    city text,
    state text,
    med_2011 integer,
    med_2014 integer
);



--
-- Name: rent; Type: TABLE; Schema: public; 
--

CREATE TABLE rent (
    neighborhood text,
    city text,
    state text,
    med_2011 integer,
    med_2014 integer
);



--
-- Data for Name: buy; Type: TABLE DATA; Schema: public; 
--

COPY buy (neighborhood, city, state, med_2011, med_2014) FROM stdin;
South Los Angeles	Los Angeles	CA	157300	251000
Sherman Oaks	Los Angeles	CA	250100	300300
Sunrise Manor	Las Vegas	NV	39000	47700
Southeast Los Angeles	Los Angeles	CA	130200	209400
Deer Valley	Phoenix	AZ	51900	72300
Far North	Dallas	TX	62000	68000
Hollywood	Los Angeles	CA	336600	404200
Williamsburg	New York	NY	484700	718600
Southeast Dallas	Dallas	TX	36600	43600
Roosevelt	Fresno	CA	46200	51200
Enterprise	Las Vegas	NV	88700	101900
East Memphis-Colonial-Yorkshire	Memphis	TN	53100	50000
Central City	Corpus Christi	TX	57000	53200
Bullard	Fresno	CA	62900	74800
Mid City	Los Angeles	CA	253000	377000
West San Jose	San Jose	CA	294000	380600
North Long Beach	Long Beach	CA	143100	199100
Sun Valley	Los Angeles	CA	186800	265900
South Scottsdale	Scottsdale	AZ	70900	114100
Canoga Park	Los Angeles	CA	137000	178900
Sylmar	Los Angeles	CA	195500	241400
Downtown	San Jose	CA	306400	421900
Pacoima	Los Angeles	CA	156800	208000
San Pedro	Los Angeles	CA	254000	255200
Willow Glen	San Jose	CA	340100	391200
West Anaheim	Anaheim	CA	159600	206900
Blossom Valley	San Jose	CA	221800	303200
West Rogers Park	Chicago	IL	83800	67700
Mira Mesa	San Diego	CA	121300	168100
Midtown	Memphis	TN	50100	59900
Cambrian Park	San Jose	CA	217100	322000
Princess Anne	Virginia Beach	VA	167300	144200
South Dorchester	Boston	MA	151600	185100
Roxbury	Boston	MA	195500	225900
Southeast Colorado Springs	Colorado Springs	CO	70700	77500
East Colorado Springs	Colorado Springs	CO	96900	104100
Green Run	Virginia Beach	VA	106100	118200
Winnetka Heights	Dallas	TX	52000	54800
Wilmington	Los Angeles	CA	194900	255700
Mission	San Francisco	CA	499800	654300
Northeast Colorado Springs	Colorado Springs	CO	77100	79700
Central Colorado Springs	Colorado Springs	CO	97400	100600
Gramercy	New York	NY	712000	800800
Fresno High Roeding	Fresno	CA	55200	71500
Rogers Park	Chicago	IL	110400	85200
Downtown	Memphis	TN	127400	126200
Kempsville	Virginia Beach	VA	101400	126700
Little Havana	Miami	FL	57300	92700
Lake Highlands	Dallas	TX	32200	37600
Lake View	Chicago	IL	175100	170600
Valencia	Santa Clarita	CA	176500	216000
Greater Uptown	Houston	TX	115900	124700
Highland Park	Los Angeles	CA	256300	379700
University City	San Diego	CA	192800	242200
Oak Lawn	Dallas	TX	114000	125200
Rancho Penasquitos	San Diego	CA	132700	172800
Winnetka	Los Angeles	CA	126200	162400
Mid City West	Los Angeles	CA	336500	407600
Brighton	Boston	MA	194400	235700
Alameda - West Flagler	Miami	FL	65500	91000
Memorial	Houston	TX	91600	107600
Woodland Hills	Los Angeles	CA	192000	250700
El Sereno	Los Angeles	CA	203300	279500
Palms	Los Angeles	CA	300500	335400
Carmel Valley	San Diego	CA	234400	301700
Allapattah	Miami	FL	51400	71000
Rancho Bernardo	San Diego	CA	149300	213100
Greater Heights	Houston	TX	201700	246900
Parkchester	New York	NY	105300	94100
River Oaks-Kirby-Balmoral	Memphis	TN	43600	49100
North Dallas	Dallas	TX	79800	82300
East Boston	Boston	MA	172700	210300
Mar Vista	Los Angeles	CA	320700	374300
Coral Way	Miami	FL	107200	190500
South End	Tacoma	WA	94500	92200
Mid Wilshire	Los Angeles	CA	284000	328700
North	Arlington	TX	46000	46700
Studio City	Los Angeles	CA	328700	359800
Crenshaw	Los Angeles	CA	202900	251800
Lake View East	Chicago	IL	165300	165500
North Park	San Diego	CA	143000	199200
Silver Lake	Los Angeles	CA	397700	554500
Venice	Los Angeles	CA	644200	894200
Kalihi-Palama	Honolulu	HI	303300	299300
Westchester	Los Angeles	CA	202900	202200
Downtown	Los Angeles	CA	272300	398100
Hyde Park	Los Angeles	CA	166300	274400
South Loop	Chicago	IL	180000	201200
Brentwood	Los Angeles	CA	404700	451500
Mattapan	Boston	MA	193100	241700
Southwest Colorado Springs	Colorado Springs	CO	107300	121500
South Boston	Boston	MA	283000	348400
Lincoln Heights	Los Angeles	CA	176400	280000
Edgewater Beach	Chicago	IL	113100	106700
North Central	Pasadena	CA	274500	351700
Del Rey	Los Angeles	CA	428300	557600
Hyde Park	Boston	MA	140700	155100
M Streets	Dallas	TX	98300	99800
Makiki-Lower Punchbowl-Tantalus	Honolulu	HI	263100	285800
The Colony	Anaheim	CA	218900	316700
Downtown	Jersey City	NJ	307000	358000
Gold  Coast	Chicago	IL	214900	218200
Columbia Heights	Washington	DC	289100	330900
Wynnefield	Philadelphia	PA	88900	61700
Hawaii Kai	Honolulu	HI	374200	419200
La Jolla	San Diego	CA	365600	395000
Sugar House	Salt Lake City	UT	177700	208400
Roslindale	Boston	MA	193100	200700
West Roxbury	Boston	MA	164300	173200
Sawtelle	Los Angeles	CA	359800	416900
Center City West	Philadelphia	PA	272400	300100
Summerlin South	Las Vegas	NV	149100	200400
Payne Phallen	Saint Paul	MN	66800	67200
Clinton	New York	NY	763300	869100
Pacific Beach	San Diego	CA	222400	269300
Capitol Hill	Seattle	WA	230700	276600
Gateway - Green Valley Ranch	Denver	CO	74300	82600
Westwood	Cincinnati	OH	59400	55200
Eastside-ENACT	Tacoma	WA	93600	94500
Financial District	New York	NY	824900	901400
Neartown - Montrose	Houston	TX	142900	150200
South End	Boston	MA	412000	502200
West End	Tacoma	WA	170600	166000
Glassell Park	Los Angeles	CA	291200	391700
Allston	Boston	MA	184900	236400
North Valleys	Reno	NV	62600	71600
Alexandria Wrest	Alexandria	VA	153800	175300
Southeast Boise	Boise	ID	95800	127100
Tierrasanta	San Diego	CA	156700	215200
Jamaica Plain	Boston	MA	208800	243100
Capitol Hill	Washington	DC	324200	365800
Brickell	Miami	FL	192900	306900
McCully-Moiliili	Honolulu	HI	285000	315500
Center City East	Philadelphia	PA	245500	253100
Eagle Rock	Los Angeles	CA	326800	445800
Los Feliz	Los Angeles	CA	339400	408900
Ravenswood	Chicago	IL	168100	154700
Nevada-Lidgerwood	Spokane	WA	67900	64200
North Linden	Columbus	OH	42100	35800
Washington Avenue Coalition - Memorial Park	Houston	TX	181900	223700
Northwest Colorado Springs	Colorado Springs	CO	111100	103800
Forest Park	Springfield	MA	68500	71400
Bernal Heights	San Francisco	CA	609900	816900
Aliamanu-Salt Lake-Foster Village	Honolulu	HI	222200	232700
University District	Seattle	WA	231000	247400
North End	Saint Paul	MN	76300	72900
South Boulevard-Park Row Historic	Dallas	TX	115700	128400
Landmark-Van Dom	Alexandria	VA	173800	190300
San Ysidro	San Diego	CA	62500	98800
Waikiki	Honolulu	HI	286500	347300
Abbott Loop	Anchorage	AK	103100	99600
South Tacoma	Tacoma	WA	92700	92400
Woodbridge	Irvine	CA	286400	330900
Highland	Saint Paul	MN	108100	119000
North End	Tacoma	WA	161100	159800
Northeast	Reno	NV	36800	42400
Powellhurst Gilbert	Portland	OR	126200	136400
West Town	Chicago	IL	226400	234800
Liliha-Kapalama	Honolulu	HI	204300	257000
Potomac West	Alexandria	VA	192900	192300
Fenway	Boston	MA	274600	334800
Linda Vista	San Diego	CA	139600	193500
Liberty City	Miami	FL	51000	63100
Manoa	Honolulu	HI	242500	295700
Hazelwood	Portland	OR	116500	117300
Sixteen Acres	Springfield	MA	94700	89400
Northwest	Spokane	WA	87600	82000
Sunland	Los Angeles	CA	252700	308800
South	Pasadena	CA	282700	333500
Fairmount-Spring Garden	Philadelphia	PA	207400	204100
West Park	Irvine	CA	249000	310600
Tujunga	Los Angeles	CA	199400	289500
Near North	Chicago	IL	207000	238200
Bayview	San Francisco	CA	360400	400700
West Central	Pasadena	CA	335900	372600
South Side	Toledo	OH	32100	34100
Seminary Hill	Alexandria	VA	137300	163700
Downtown	San Francisco	CA	406800	577100
West Las Vegas	Las Vegas	NV	37400	50200
Back Bay	Boston	MA	430800	518900
Central	Tacoma	WA	116500	100600
South of Market	San Francisco	CA	492600	702000
Northwood	Irvine	CA	206600	285200
Hellman	Long Beach	CA	118700	162200
Scripps Ranch	San Diego	CA	163500	185100
Diamond Head-Kapahulu-St. Louis	Honolulu	HI	359500	431700
Lents	Portland	OR	121200	142100
Hampden	Denver	CO	70800	75000
Cal Young	Eugene	OR	121500	113400
Wynwood - Edgewater	Miami	FL	154300	270200
Elkhorn	Omaha	NE	367500	391800
Heartland Village	New York	NY	201300	199300
West Price HIll	Cincinnati	OH	50900	45200
Okolona	Louisville	KY	102100	109000
East Tampa	Tampa	FL	30500	36700
Petworth	Washington	DC	178900	208700
Pacific Heights	San Francisco	CA	636900	812000
Hyde Park	Chicago	IL	115500	97800
Nob Hill	San Francisco	CA	567700	736100
Bucktown	Chicago	IL	227200	248200
Broadmoor, Anderson Island, Shreve Isle.	Shreveport	LA	78300	89000
Downtown	Stamford	CT	167100	167100
Magnolia	Seattle	WA	176500	190700
Nuuanu-Punchbowl	Honolulu	HI	301700	331000
Mount Washington	Los Angeles	CA	313000	431100
Ala Moana-Kakaako	Honolulu	HI	342700	379500
Kenmore	Boston	MA	257700	340800
Dayton's Bluff	Saint Paul	MN	63700	66500
Old Colorado City	Colorado Springs	CO	105000	116400
South Weymouth	Weymouth	MA	136800	137600
Mission Hill	Boston	MA	242500	290400
Noe Valley	San Francisco	CA	655700	809100
Downtown	Houston	TX	155100	193800
Midtown	Atlanta	GA	139100	149300
Ellet	Akron	OH	40200	43200
Charlestown	Boston	MA	339000	405900
Logan Circle	Washington	DC	377000	434200
Greater Avenues	Salt Lake City	UT	156300	164500
Adams Morgan	Washington	DC	327700	367400
Bay View	Milwaukee	WI	121200	111400
Seatack	Virginia Beach	VA	135400	132100
Kenmore	Akron	OH	44300	39500
University Village - Little Italy	Chicago	IL	185300	205200
Washington Highlands	Washington	DC	125400	207500
Fishtown	Philadelphia	PA	258500	238100
Summit-University	Saint Paul	MN	128900	126600
Greenwood	Seattle	WA	177200	204300
Playa Del Rey	Los Angeles	CA	285800	342100
Montavilla	Portland	OR	167800	198000
Wallingford	Seattle	WA	265100	316100
CUF	Cincinnati	OH	46300	51700
University Place	Houston	TX	122100	129800
Westwood	Denver	CO	87300	96900
Desert Shores	Las Vegas	NV	42600	60000
O'Hare	Chicago	IL	83600	71400
West University	Austin	TX	149300	148100
Centerville	Fremont	CA	138600	242400
Oleander Sunset	Bakersfield	CA	44200	55200
West Side	Saint Paul	MN	88600	82000
Gandy-Sun Bay South	Tampa	FL	70700	91400
East Side	Long Beach	CA	180500	212200
West Colorado Springs	Colorado Springs	CO	111200	112100
Thomas Dale	Saint Paul	MN	64000	70900
Traffic Circle	Long Beach	CA	192800	235100
East Weymouth	Weymouth	MA	159800	173400
Capitol Hill	Denver	CO	118100	136800
Flamingo Lummus	Miami Beach	FL	157100	244200
New Tacoma	Tacoma	WA	194400	154800
Bluffview	Dallas	TX	95000	103600
Dupont Circle	Washington	DC	339100	380700
Poplar Grove	Salt Lake City	UT	107200	121600
Sixteenth Street Heights	Washington	DC	194400	258100
Lincoln Park	Chicago	IL	220700	232500
Hampden South	Denver	CO	67400	66300
Russian Hill	San Francisco	CA	681400	873200
St.Johns	Portland	OR	152200	180300
Lincoln Heights	Spokane	WA	84400	82400
Hillcrest	San Diego	CA	208800	292600
Central Weymouth	Weymouth	MA	131200	137800
Near West Side	Chicago	IL	216500	234700
Shadyside	Pittsburgh	PA	108300	115800
Georgetown	Washington	DC	430300	474300
Beverly Glen	Los Angeles	CA	670600	853200
Downtown	Miami	FL	201200	322200
Afton Oaks - River Oaks Area	Houston	TX	155100	191700
Whittier	Minneapolis	MN	76200	66900
Northwest	Portland	OR	221700	247400
City Center	Glendale	CA	198600	244200
Cove - East Side	Stamford	CT	149600	129400
Hayes Valley	San Francisco	CA	521700	665100
Downtown	Atlanta	GA	98500	88900
Caddo Heights, South Highlands	Shreveport	LA	48000	55100
Downtown	Honolulu	HI	271800	312600
Cully	Portland	OR	168400	207900
Downtown	Long Beach	CA	158800	206400
Windy Hill	Jacksonville	FL	57300	65600
Marina	San Francisco	CA	601400	747300
Foggy Bottom	Washington	DC	309500	319400
Brentwood-Darlington	Portland	OR	130700	147500
Washington Virginia Vale	Denver	CO	79000	94500
Mid-Cambridge	Cambridge	MA	298000	364600
West Side	Stamford	CT	202000	184300
Glenbrook	Stamford	CT	165900	140600
South Lakes Dr - Soapstone Dr	Reston	VA	161100	193800
Hyde Park	Cincinnati	OH	83700	70500
Van Ness - Civic Center	San Francisco	CA	428000	571400
Five Points	Denver	CO	202600	240800
Riverside	Cambridge	MA	339000	407400
Ocean Beach	San Diego	CA	354300	424900
South End	Hartford	CT	71000	69300
West Los Angeles	Los Angeles	CA	339700	404200
Downtown	Bellevue	WA	316800	378300
East Price Hill	Cincinnati	OH	38700	42400
Belmont Heights	Long Beach	CA	218700	263900
Chevy Chase	Washington	DC	271300	285900
Cambridgeport	Cambridge	MA	298500	360700
Windsor	Denver	CO	61800	68800
Park West	Chicago	IL	197200	196000
Spenard	Anchorage	AK	119700	126400
Downtown	Portland	OR	204300	228100
North Cambridge	Cambridge	MA	287900	342600
Lowry Park Central	Tampa	FL	44000	49100
Turn of River	Stamford	CT	315200	297700
North Hill	Spokane	WA	70500	72700
Fremont	Seattle	WA	201800	225100
Schuylkill Southwest	Philadelphia	PA	291600	324500
Overlake	Bellevue	WA	132800	127600
South Beach	San Francisco	CA	586600	805100
Riverwest	Milwaukee	WI	115500	116900
Ballston-Virginia Square	Arlington	VA	341500	373700
Amber Hills	San Bernardino	CA	48700	53500
Russian Jack Park	Anchorage	AK	102600	101100
North-East Coconut Grove	Miami	FL	119900	185700
Ravenna	Seattle	WA	257300	301600
Mercury Central	Hampton	VA	61200	54900
Manayunk	Philadelphia	PA	211800	200500
East Central	Spokane	WA	71100	65800
Lower East Side	Milwaukee	WI	148400	143200
North Beacon Hill	Seattle	WA	187100	182100
Shawnee	Louisville	KY	49800	56200
First Hill	Seattle	WA	200500	219400
Lower Pacific Heights	San Francisco	CA	443500	593700
Sulphur Springs	Tampa	FL	32800	39900
Buena Park	Chicago	IL	149100	139600
Mount Pleasant	Washington	DC	294600	317800
The Loop	Chicago	IL	190600	207500
North Ridge-Rosemont	Alexandria	VA	237600	235100
Aurora Highlands	Aurora	CO	42500	51600
Eureka Valley - Dolores Heights - Castro	San Francisco	CA	602500	818500
Aurora Highlands	Arlington	VA	322700	350300
North Hyde Park	Tampa	FL	106500	114300
Admiral	Seattle	WA	202100	183800
Battery Park	New York	NY	489500	545900
Peabody	Cambridge	MA	309100	381300
Radnor-Ft Myer Heights	Arlington	VA	353400	386000
Myers Park	Charlotte	NC	163200	173300
Western Addition	San Francisco	CA	368000	606000
Speer	Denver	CO	122500	134200
East Village	Long Beach	CA	133100	178600
Maple Leaf	Seattle	WA	214800	243000
Sellwood-Moreland	Portland	OR	256200	314200
Olde Torrance	Torrance	CA	235100	248300
Potrero Hill	San Francisco	CA	487100	652800
Old Town	Chicago	IL	178600	195700
Normal Heights	San Diego	CA	104500	161100
West 7th	Saint Paul	MN	88700	84700
North Oakland	Pittsburgh	PA	102800	102600
North Panhandle	San Francisco	CA	484000	612100
East Colfax	Denver	CO	104700	117900
College East	San Diego	CA	80000	130300
Bridle Trails	Bellevue	WA	123900	120500
Sabre Springs	San Diego	CA	126600	181500
Congress Park	Denver	CO	109300	129400
University Area	Anchorage	AK	117100	114100
Mission Valley East	San Diego	CA	133400	213400
Mission Bay Park	San Diego	CA	253800	310500
Kingman Park	Washington	DC	181300	248500
Kingsgate	Kirkland	WA	125900	118200
North End	Boston	MA	362400	420400
Fairlington-Shirlington	Arlington	VA	355200	365700
North Queen Anne	Seattle	WA	182300	202200
Montclaire South	Charlotte	NC	49800	53200
Old Louisville	Louisville	KY	70300	84300
College Hill	Providence	RI	208600	203000
Warm Springs	Fremont	CA	186700	261300
Sunset Hills	Reston	VA	230200	299900
Verdugo Viejo	Glendale	CA	215800	265300
West Colfax	Denver	CO	122200	153900
Belmont	Dayton	OH	44600	41000
Sunnyside	Denver	CO	179400	232600
East Cambridge	Cambridge	MA	374400	451300
American University Park	Washington	DC	420500	461900
Wrightwood Neighbors	Chicago	IL	222900	236800
Concordia	Portland	OR	223200	269900
Central City	Salt Lake City	UT	129500	140900
Ohio City - West Side	Cleveland	OH	116800	80600
University	Denver	CO	196100	243800
Mustang-Padre Island	Corpus Christi	TX	93200	105600
East Bench	Salt Lake City	UT	216500	214400
Shaw	Washington	DC	352200	398800
Belltown	Seattle	WA	274900	313200
Beacon Hill	Boston	MA	366400	458300
Chinatown	Boston	MA	441200	541400
North End	Boise	ID	159200	188000
Southwest Waterfront	Washington	DC	228900	263500
Douglas Park	Arlington	VA	313700	321100
Woodstock	Portland	OR	198900	232200
Phinney Ridge	Seattle	WA	282400	326800
Cleveland Park	Washington	DC	316300	330300
Villa Park	Denver	CO	99200	115300
Isle of Normandy	Miami Beach	FL	76700	139500
Bear Valley	Denver	CO	64500	71700
West Highland	Denver	CO	216400	271300
Emerson-Garfield	Spokane	WA	66700	65100
Madisonville	Cincinnati	OH	58200	52200
Golden Hill	San Diego	CA	96300	172700
Highland	Denver	CO	196100	248600
West Cambridge	Cambridge	MA	343100	398400
Rossmoyne	Glendale	CA	211700	260300
Green Lake	Seattle	WA	280500	319700
Riverside	Jacksonville	FL	132900	145100
Highland Park	Des Moines	IA	59600	61300
Northeast Macfarlane	Tampa	FL	55300	56500
Haller Lake	Seattle	WA	147200	133800
Fort Logan	Denver	CO	88600	80600
Riverbend	Columbus	OH	50900	49600
Cow Hollow	San Francisco	CA	648800	817300
Park West	San Diego	CA	271900	359300
Manor Park	Washington	DC	177200	\N
Bitter Lake	Seattle	WA	165500	123500
Near Northeast	Washington	DC	286300	338400
Grantville	San Diego	CA	116700	161200
Cliff-Cannon	Spokane	WA	84600	71200
Berkeley	Denver	CO	201200	250200
Lowry Field	Denver	CO	156700	188800
Morningside - Lenox Park	Atlanta	GA	120800	121700
Vose	Beaverton	OR	80900	73100
Beechmont	Louisville	KY	85400	82900
Downtown	Saint Paul	MN	115600	103100
Creston-Kenilworth	Portland	OR	212600	234400
East Village	San Diego	CA	287000	374000
Capitol Hill	Salt Lake City	UT	176800	182200
Carriage Place	Aurora	CO	45700	59000
South Juanita	Kirkland	WA	137200	139500
Cheesman Park	Denver	CO	128400	144100
Clarendon-Courthouse	Arlington	VA	381200	439800
Loring Park	Minneapolis	MN	135200	141300
River North	Chicago	IL	225500	249100
Loyal Heights	Seattle	WA	257300	346000
Downtown	New York	NY	476000	528900
Kenton	Portland	OR	158000	189000
Minor	Seattle	WA	224600	243800
Expo Park	Aurora	CO	42100	47200
Linden Hills	Minneapolis	MN	166100	179800
Bemiss	Spokane	WA	73400	64100
Glover Park	Washington	DC	271300	284700
Telegraph Hill	San Francisco	CA	616500	805700
Old Town Triangle	Chicago	IL	230200	243500
Forest Hills	Tampa	FL	56700	60500
Family Acres	Lincoln	NE	290500	312600
Northside	Cincinnati	OH	42300	55600
Multnomah	Portland	OR	196900	239600
Somerset	Columbus	OH	45900	36300
University Park	Denver	CO	123100	136200
Ballard	Seattle	WA	230400	281800
Mount Scott	Portland	OR	151900	183500
Foster-Powell	Portland	OR	151100	185900
Wilburton	Bellevue	WA	186800	212000
Starmount Forest	Charlotte	NC	46500	57200
Downtown	Austin	TX	261100	339900
Virginia Highland	Atlanta	GA	133500	124900
Sloan Lake	Denver	CO	209700	265600
Old Town	Alexandria	VA	341800	353200
Dayton Triangle	Aurora	CO	71400	88000
Fairview	Anchorage	AK	131800	132700
Alki	Seattle	WA	274400	311500
Springdale	Stamford	CT	170900	157400
Downtown	Seattle	WA	381000	446500
Corbett-Terwilliger-Lair Hill	Portland	OR	230700	250500
Old Seminole Heights	Tampa	FL	45600	57700
Margate Park	Chicago	IL	98300	92500
Metro Center	Springfield	MA	67000	72700
Crescent Hill	Louisville	KY	154900	190400
East Queen Anne	Seattle	WA	230500	260600
Taylor Berry	Louisville	KY	55500	54700
Washington Park	Denver	CO	173700	188800
North College Park	Seattle	WA	150400	139700
Hale	Denver	CO	74500	89300
Columbia Heights West	Arlington	VA	163900	176100
Teralta East	San Diego	CA	75200	114800
Howe	Minneapolis	MN	124700	136100
Victoria Park	Fort Lauderdale	FL	91200	128500
Mount Vernon Square	Washington	DC	363700	430800
Over-The-Rhine	Cincinnati	OH	128000	152000
Dilworth	Charlotte	NC	142200	160900
California Heights	Long Beach	CA	110800	139900
South Dennis	Dennis	MA	109800	117800
Southside Flats	Pittsburgh	PA	152900	163200
Piedmont Avenue	Oakland	CA	247600	256600
Walnut Hills	Cincinnati	OH	112700	101500
Bellmont Hillsboro	Nashville	TN	203900	238400
Standish	Minneapolis	MN	114400	118300
College View - South Platte	Denver	CO	67400	73400
Sunset Hill	Seattle	WA	331900	354300
Arbor Lodge	Portland	OR	188500	225700
University Hill	Boulder	CO	185000	204300
Montrose Verdugo City	Glendale	CA	219200	251300
Gatewood	Seattle	WA	179100	209900
Goose Hollow	Portland	OR	194600	236500
Elyria Swansea	Denver	CO	80400	98600
Washington Park West	Denver	CO	210700	247000
College Downs	Charlotte	NC	63900	58500
Downtown	Columbus	OH	96300	102600
Overlook	Portland	OR	196100	242900
Roseway	Portland	OR	178400	221500
The Museum District	Richmond	VA	144900	147600
King	Portland	OR	214500	269800
North Rose Hill	Kirkland	WA	127900	124900
Lowry Hill East	Minneapolis	MN	89200	76600
The Port - Area 4	Cambridge	MA	306400	382400
Lincoln Park	Denver	CO	144000	170900
Ingleside Heights	San Francisco	CA	264700	384800
Forest Hills	Washington	DC	269500	305100
Barnum	Denver	CO	92700	108600
Central Downtown	Lexington	KY	116300	116400
Chickasaw	Louisville	KY	48800	55600
Fairpark	Salt Lake City	UT	110600	144200
Penn Wynne	Wynnewood	PA	94300	100200
La Jolla Village	San Diego	CA	237200	285600
Columbia Heghts	Arlington	VA	271700	293500
North Towne	Toledo	OH	45800	52900
Junction	Seattle	WA	230000	251100
Lynnhaven Shores	Virginia Beach	VA	162200	156700
West Queen Anne	Seattle	WA	223700	238200
Ballast Point	Tampa	FL	72100	90100
Old West Tampa	Tampa	FL	56600	63600
Johnston Rd.-McAlpine	Charlotte	NC	48500	52200
North Capitol Hill	Denver	CO	185700	199900
Marshall Heights	Washington	DC	135800	164000
Goldsmith	Denver	CO	62700	70200
Bayshore	Miami Beach	FL	249700	362200
Pearl District	Portland	OR	266300	320000
Branford Center	Branford	CT	95300	81100
Side Creek	Aurora	CO	52700	71600
Smith Hill	Providence	RI	176900	139900
Southwest Hills	Portland	OR	438200	547100
Arlington Ridge	Arlington	VA	252500	262100
Downtown West	Minneapolis	MN	108000	117300
Meadow Hills	Aurora	CO	64900	80700
Century City	Los Angeles	CA	417800	550500
Highline Villages	Aurora	CO	49400	57400
West End	Boston	MA	364800	426000
Cherry Creek	Denver	CO	182400	233000
Eastlake	Seattle	WA	245700	293100
Southside	Louisville	KY	87900	87200
West Loop Gate	Chicago	IL	196200	216100
Totem Lake	Kirkland	WA	131000	124400
Hiawatha	Minneapolis	MN	126200	131700
Wexford-Thornapple	Columbus	OH	56600	57500
Montclair	Denver	CO	132500	145600
Platt Park	Denver	CO	229300	280200
Rose Village	Vancouver	WA	90500	96800
City Center North	Aurora	CO	43300	48100
Sterling Hills	Aurora	CO	82800	97900
Buckingham	Arlington	VA	216900	236600
Braddock Road Metro	Alexandria	VA	313200	365100
City Center	Aurora	CO	41000	44900
Folwell	Minneapolis	MN	67600	73000
Pinehurst	Seattle	WA	165100	145800
Edgewood	Washington	DC	169100	197000
Lower Queen Anne	Seattle	WA	235800	261200
East Ridge - Ptarmigan Park	Aurora	CO	56900	60600
Woodley Park	Washington	DC	357600	381200
Near East Side	Chicago	IL	301200	357700
Marble Cliff Crossing	Columbus	OH	74200	59900
Heather Gardens	Aurora	CO	67400	93600
Columbia Forest	Arlington	VA	156600	160800
Galt Mile	Fort Lauderdale	FL	188500	240800
Business District	Irvine	CA	252200	344100
Leschi	Seattle	WA	250100	306800
Lyon Park	Arlington	VA	263500	273600
Coral Ridge Country Club	Fort Lauderdale	FL	79900	109700
Fox Point	Providence	RI	164400	158500
The North End	Virginia Beach	VA	226600	222700
Bloomingdale	Washington	DC	214400	290000
Bluff Heights	Long Beach	CA	189000	232700
North Central	San Mateo	CA	262300	382700
Juneau Town	Milwaukee	WI	144100	126600
Jacobs	Louisville	KY	55800	52600
Marina	San Diego	CA	333000	418100
Fairground	Des Moines	IA	51700	56800
Whittier	Boulder	CO	166700	195700
City Park West	Denver	CO	129500	160700
Whittier	Denver	CO	172000	210900
Fort Sanders	Knoxville	TN	37300	43200
Yerba Buena	San Francisco	CA	492600	728800
Baker	Denver	CO	169800	195100
Barclay Downs	Charlotte	NC	148200	142200
Clifton Heights	Louisville	KY	99700	115300
Summer Valley	Aurora	CO	108800	133600
Downtown	Lincoln	NE	98300	98000
Iroquois	Louisville	KY	69000	65800
South Addition	Anchorage	AK	158600	157800
Prescott	Oakland	CA	296200	345900
Cole	Denver	CO	127600	155100
Marina Area	Long Beach	CA	267800	382400
Westlake	Seattle	WA	220900	247500
North Loop	Minneapolis	MN	194600	214000
Southside Slopes	Pittsburgh	PA	54900	60300
Seaview	Seattle	WA	240600	270400
Victorian Village	Columbus	OH	125800	145800
SableRidge	Aurora	CO	41200	49300
Regency	Jacksonville	FL	40100	38700
Mission Beach	San Diego	CA	601600	631800
Cotswold	Charlotte	NC	75200	75000
Wesley Heights	Washington	DC	263200	253300
Harbour Island	Tampa	FL	126000	158300
Uptown	Seattle	WA	229400	262600
Madison Park	Seattle	WA	284100	317200
Jefferson Park	Charlottesville	VA	131400	119100
View Ridge	Seattle	WA	155900	156900
Streeterville	Chicago	IL	299900	327200
Union Station	Denver	CO	300300	335100
East Merrimack	Merrimack	NH	101600	93000
Rancho San Joaquin	Irvine	CA	402000	505000
Belcaro	Denver	CO	223100	252600
Elizabeth	Charlotte	NC	97700	115900
City Center	Miami Beach	FL	185200	273000
Belknap	Louisville	KY	202200	230400
Peachtree Heights West	Atlanta	GA	111700	106700
Schnitzelburg	Louisville	KY	89300	104600
Cahuenga Pass	Los Angeles	CA	564500	710300
Mission Hills	Henderson	NV	81200	95800
Downtown	Washington	DC	363400	421500
Minnehaha	Minneapolis	MN	119400	124800
Deer Park	Louisville	KY	166000	188700
Tollgate Overlook	Aurora	CO	41000	47500
Sequoyah	Oakland	CA	194600	218800
Wyandotte	Louisville	KY	55600	56800
Central Beach Alliance	Fort Lauderdale	FL	141800	186100
Audubon	Louisville	KY	117400	125300
Sharon Woods	Charlotte	NC	69100	68100
Regis	Denver	CO	171400	200600
Village Shires	Northampton Township	PA	158600	143700
South Louisville	Louisville	KY	49500	57200
Park Duvalle	Louisville	KY	41500	45800
El Dorado Park Estates	Long Beach	CA	171200	187400
Fourth Ward	Charlotte	NC	177400	207300
Hikes Point	Louisville	KY	137600	144000
Germantown	Louisville	KY	79500	94300
Stapleton	Denver	CO	152400	170300
Centretech	Aurora	CO	42100	47800
Cherokee Triangle	Louisville	KY	164000	197900
Edgewood	Atlanta	GA	138900	140200
Inman Park	Atlanta	GA	152600	161500
Playa Vista	Los Angeles	CA	358900	421500
Heather Ridge	Aurora	CO	70300	80500
U Street Corridor	Washington	DC	397600	459300
Globeville	Denver	CO	79400	102000
North Delridge	Seattle	WA	191500	202500
Central Business District	Denver	CO	216900	265900
Fulton River District	Chicago	IL	218000	236000
Eisenhower East	Alexandria	VA	354400	370300
Central Business District	Orlando	FL	59600	108900
Moss Bay	Kirkland	WA	275300	305600
Town Center	Reston	VA	130000	162000
Central Business District	Pittsburgh	PA	92300	117300
Cathedral Heights	Washington	DC	281300	278600
Central Business District - Downtown	Kansas City	MO	138400	156800
Downtown	Salt Lake City	UT	201900	224100
Sylvan Park	Nashville	TN	135600	169100
Old Town-Chinatown	Portland	OR	163000	188400
South Salt Creek	Lincoln	NE	50600	56800
Northcrest	Columbus	OH	46800	51600
Candler Park	Atlanta	GA	128000	123000
West End	Washington	DC	447700	511700
Navy Yard	Washington	DC	404800	485900
Yankee Hill	Milwaukee	WI	180000	158200
North Highland	Arlington	VA	267900	261100
Downtown	Boston	MA	453100	575900
Alamitos Heights	Long Beach	CA	193700	220200
Indian Creek	Denver	CO	126100	129000
Conway	Orlando	FL	30500	36900
Bluff Park	Long Beach	CA	208200	274600
East Isles	Minneapolis	MN	109400	126600
Keewaydin	Minneapolis	MN	92400	107600
City Park	Denver	CO	208400	239400
Chinatown	Oakland	CA	245200	278400
Esther Short	Vancouver	WA	138000	134900
Wakefield	Washington	DC	275900	300500
The Palisades	Washington	DC	252300	248300
Highlands Douglas	Louisville	KY	183500	212200
Park East	Sarasota	FL	40800	50700
Clearwater Beach Association	Clearwater	FL	172400	191300
Waverly Hills	Arlington	VA	218700	231800
North Campus	Columbus	OH	67100	74800
Cedar-Isles-Dean	Minneapolis	MN	195800	198600
Shelby Park	Louisville	KY	54100	66200
Ashbrook-Clawson Village	Charlotte	NC	115700	94200
Guide Meridian	Bellingham	WA	124700	119000
First Ward	Charlotte	NC	133300	148000
Dennis Port	Dennis	MA	145400	127800
The Strip	Las Vegas	NV	214300	251600
Mission Valley West	San Diego	CA	189000	228900
Morris Park	Minneapolis	MN	107200	113900
North Rosslyn	Arlington	VA	379600	428700
Saint Joseph	Louisville	KY	84200	94100
Denny Triangle	Seattle	WA	310400	396100
Buena Vista Park	San Francisco	CA	483400	657100
Clifton	Louisville	KY	113200	129600
Downtown Des Moines	Des Moines	IA	89800	80300
Smoketown Jackson	Louisville	KY	52600	67000
Downtown Charlotte	Charlotte	NC	189600	228700
Brightwood Park	Washington	DC	151400	174600
Colonial Village	Arlington	VA	277700	292200
White Bridge	Nashville	TN	73300	86900
Tyler Park	Louisville	KY	144300	164200
Livingston - McNaughten	Columbus	OH	35200	33100
Wilder Park	Louisville	KY	64200	68700
Mapleton Hill	Boulder	CO	170600	189600
Kalorama	Washington	DC	377400	429500
Hazelwood	Louisville	KY	50000	62400
Produce & Waterfront	Oakland	CA	209100	314200
Brownsboro Zorn	Louisville	KY	154100	167900
Carver City	Tampa	FL	55200	76700
Diamond Heights	San Francisco	CA	299600	420100
Dearborn Park	Chicago	IL	195500	192000
East Aurora	Boulder	CO	103200	114300
Overland	Denver	CO	127200	155000
Third Ward	Charlotte	NC	157600	155900
Lake View	Kirkland	WA	250400	275400
Judiciary Square	Washington	DC	414700	473500
Bonnycastle	Louisville	KY	181800	220100
Castleberry Hill	Atlanta	GA	131100	114700
South Eola	Orlando	FL	125200	195100
German Village Commission	Columbus	OH	166200	193300
Channel District	Tampa	FL	124000	174900
Fifeville	Charlottesville	VA	148000	158800
Printers Row	Chicago	IL	197500	206600
Downtown	West Palm Beach	FL	118400	188700
Rock Creek Lexington Road	Louisville	KY	190800	224500
Riverfront	Philadelphia	PA	267400	292000
Central Cocoanut	Sarasota	FL	160500	206800
Ridgedale Park	Atlanta	GA	122900	113400
Central College	Columbus	OH	74200	67300
Hawthorne	Louisville	KY	145300	169500
Atlantic Station	Atlanta	GA	99400	139400
Belle Isle	Miami Beach	FL	222800	336600
Central Waterfront - Dogpatch	San Francisco	CA	534900	741600
Ansley Park	Atlanta	GA	133200	137500
Fremont Park	Glendale	CA	181500	225300
Heritage Eagle Bend	Aurora	CO	321700	368900
Tampa-Bayshore Gardens	Tampa	FL	133800	131900
Poplar Level	Louisville	KY	123500	136600
Buckhead Village	Atlanta	GA	134600	150200
Old Town North	Alexandria	VA	266300	293200
McLean Gardens	Washington	DC	345000	353700
Civic Center	Denver	CO	260300	302200
Camp Taylor	Louisville	KY	91200	100900
South Orange	Orlando	FL	68200	77300
Prestonia	Louisville	KY	97500	113300
Downtown	Tampa	FL	147500	196700
Fairfax Village	Washington	DC	120600	152800
Hayden Island	Portland	OR	128800	156400
Highlands	Louisville	KY	113100	131700
Merriwether	Louisville	KY	74200	85900
Bethlehem	Augusta	GA	34100	31300
Downtown Knoxville	Knoxville	TN	161300	148800
Chantilly	Charlotte	NC	73700	78800
Penn Quarter	Washington	DC	391500	439100
Gardiner Lane	Louisville	KY	192300	219300
Sunrise Intracoastal	Fort Lauderdale	FL	125900	184400
Girdwood	Anchorage	AK	215300	190000
Northeast	Alexandria	VA	225300	223200
Lido Key	Sarasota	FL	223700	249200
Cabbagetown	Atlanta	GA	125100	157700
Historic Third Ward	Milwaukee	WI	208700	221100
New Horizons South Bay	Torrance	CA	304400	343200
Germantown	Nashville	TN	151500	182500
North Golf Estates	Fort Lauderdale	FL	58000	74500
Harbour Isles	Fort Lauderdale	FL	306900	351500
Bay Colony Club	Fort Lauderdale	FL	82200	122100
Keewaydin	Boulder	CO	133700	151800
Hillcrest	Hollywood	FL	40100	56000
North Weymouth	Weymouth	MA	177300	181300
Ponderosa	Sunnyvale	CA	270300	379700
Sunset	Renton	WA	111000	101100
Emerald Hills	Hollywood	FL	86200	108900
Hollywood Lakes	Hollywood	FL	63100	73100
North Shore	Miami Beach	FL	110700	194700
Old City	Philadelphia	PA	269800	269900
South Central Beach	Hollywood	FL	136000	205500
Oceanfront	Miami Beach	FL	228000	318700
Nautilus	Miami Beach	FL	174300	226900
South Pointe	Miami Beach	FL	255200	344800
\.


--
-- Data for Name: rent; Type: TABLE DATA; Schema: public; Owner: moses
--

COPY rent (neighborhood, city, state, med_2011, med_2014) FROM stdin;
Northeast Dallas	Dallas	TX	825	985
Paradise	Las Vegas	NV	900	1100
Maryvale	Phoenix	AZ	795	850
Upper West Side	New York	NY	2795	3300
South Los Angeles	Los Angeles	CA	1150	1400
Sherman Oaks	Los Angeles	CA	1399	1450
Upper East Side	New York	NY	2250	2700
Sunrise Manor	Las Vegas	NV	800	895
East New York	New York	NY	1350	1500
Southeast Los Angeles	Los Angeles	CA	1200	1300
Spring Valley	Las Vegas	NV	1029	1150
Deer Valley	Phoenix	AZ	899	1100
Astoria	New York	NY	1550	2143
Paradise Valley	Phoenix	AZ	1000	1150
North Mountain	Phoenix	AZ	750	850
Washington Heights	New York	NY	1395	1750
Far North	Dallas	TX	762	1050
Hollywood	Los Angeles	CA	1600	1750
Williamsburg	New York	NY	2200	2900
Bedford Stuyvesant	New York	NY	1500	2150
Camelback East	Phoenix	AZ	886	985
Flatbush	New York	NY	1275	1675
East Side	El Paso	TX	700	975
Southeast Dallas	Dallas	TX	950	950
Crown Heights	New York	NY	1500	2100
Alahambra	Phoenix	AZ	700	740
Jamaica	New York	NY	1400	1545
Roosevelt	Fresno	CA	715	695
Williamsbridge	New York	NY	1200	1200
North Scottsdale	Scottsdale	AZ	1800	1750
East Harlem	New York	NY	1975	2500
East San Jose	San Jose	CA	1545	2300
East Flatbush	New York	NY	1250	1700
Harlem	New York	NY	1600	1900
Bushwick	New York	NY	1575	2300
South Mountain	Phoenix	AZ	895	995
Corona	New York	NY	1400	1500
Enterprise	Las Vegas	NV	1200	1200
Concourse	New York	NY	1150	1350
East Memphis-Colonial-Yorkshire	Memphis	TN	795	725
Sunset Park	New York	NY	1500	1600
Alief	Houston	TX	649	899
South Side	Corpus Christi	TX	800	1595
North Hollywood	Los Angeles	CA	1610	1600
Elmhurst	New York	NY	1375	1615
Borough Park	New York	NY	1500	1600
Central City	Corpus Christi	TX	700	999
Bullard	Fresno	CA	850	1100
Mid City	Los Angeles	CA	1675	1950
Bensonhurst	New York	NY	1350	1400
Southwest Dallas	Dallas	TX	909	1100
West San Jose	San Jose	CA	1325	2395
Northeast	El Paso	TX	780	925
East	Arlington	TX	740	995
Westlake	Los Angeles	CA	1644	1395
Koreatown	Los Angeles	CA	1100	1150
North Long Beach	Long Beach	CA	1294	1250
White Haven-Coro Lake	Memphis	TN	740	750
Soundview	New York	NY	1050	1375
Sun Valley	Los Angeles	CA	1250	2000
Lower East Side	New York	NY	2300	2895
Logan Square	Chicago	IL	1100	1295
South Bronx	New York	NY	1350	1500
Northwest	El Paso	TX	785	1295
Southeast	Arlington	TX	1100	1300
South Scottsdale	Scottsdale	AZ	1200	1395
Flushing	New York	NY	1450	1650
Preston Hollow	Dallas	TX	1100	1350
Canarsie	New York	NY	1400	1600
Little Village	Chicago	IL	850	950
Estrella	Phoenix	AZ	950	945
Canoga Park	Los Angeles	CA	1750	1925
Boyle Heights	Los Angeles	CA	\N	1475
Sylmar	Los Angeles	CA	1300	1995
Downtown	San Jose	CA	1550	2336
Ahwatukee Foothills	Phoenix	AZ	999	1375
West	Arlington	TX	820	1050
Pacoima	Los Angeles	CA	1150	1800
Gravesend	New York	NY	1450	1500
Evergreen	San Jose	CA	2389	2499
Sharpstown	Houston	TX	630	1200
San Pedro	Los Angeles	CA	1350	1395
North Valley	San Jose	CA	1700	2232
Sheepshead Bay	New York	NY	1275	1527
Murray Hill	New York	NY	1600	1700
Willow Glen	San Jose	CA	1455	2022
North Raleigh	Raleigh	NC	895	1050
South Ozone Park	New York	NY	1550	1595
Southwest	Chula Vista	CA	1400	1550
Northridge	Los Angeles	CA	1690	1766
West Anaheim	Anaheim	CA	1275	1405
Forest Hills	New York	NY	1500	1925
East Village	New York	NY	2650	3000
Eldridge - West Oaks	Houston	TX	909	1452
Cordova-Appling	Memphis	TN	899	1150
Blossom Valley	San Jose	CA	1625	1898
Jackson Heights	New York	NY	1400	1700
Northwest Raleigh	Raleigh	NC	905	1250
Far Rockaway	New York	NY	1395	1350
Ridgewood	New York	NY	1400	1700
West Rogers Park	Chicago	IL	950	1100
Reseda	Los Angeles	CA	1950	2100
Mira Mesa	San Diego	CA	1495	1705
East Elmhurst	New York	NY	1495	1800
Midtown	Memphis	TN	730	645
Cambrian Park	San Jose	CA	1425	1850
Hickory Ridge-South Riverdale	Memphis	TN	649	950
Panorama City	Los Angeles	CA	1275	1495
Princess Anne	Virginia Beach	VA	1575	1550
Midwood	New York	NY	1300	1395
Central Southwest	Houston	TX	1025	1080
North Hills	Los Angeles	CA	1995	1575
South Dorchester	Boston	MA	1575	1700
Roxbury	Boston	MA	1600	1900
South Belt - Ellington	Houston	TX	750	1267
Southeast Colorado Springs	Colorado Springs	CO	825	975
Clear Lake	Houston	TX	755	1300
Northside-Northline	Houston	TX	\N	1175
Park Slope	New York	NY	2095	2700
Cedar Crest	Dallas	TX	750	775
Oxford Circle	Philadelphia	PA	850	950
East Colorado Springs	Colorado Springs	CO	900	1000
Northeast Raleigh	Raleigh	NC	850	1050
Green Run	Virginia Beach	VA	1150	1150
Winnetka Heights	Dallas	TX	\N	789
Wilmington	Los Angeles	CA	1500	1200
Mission	San Francisco	CA	2350	3500
Archer Heights	Chicago	IL	1050	1100
Bath Beach	New York	NY	1350	1500
Northeast Colorado Springs	Colorado Springs	CO	999	1150
Central Colorado Springs	Colorado Springs	CO	765	795
Raleigh	Memphis	TN	729	825
Woodward Park	Fresno	CA	1000	1299
Kingwood Area	Houston	TX	930	1000
Greater Fondren Southwest	Houston	TX	675	825
Central City	Phoenix	AZ	749	795
Gramercy	New York	NY	2750	3200
South Austin	Chicago	IL	850	823
Brownsville	New York	NY	1276	1400
Lower Valley	El Paso	TX	\N	895
Encino	Los Angeles	CA	2100	2035
Ozone Park	New York	NY	1400	1599
The Heights	Jersey City	NJ	1350	1500
Fresno High Roeding	Fresno	CA	695	650
Tremont	New York	NY	975	1235
Rogers Park	Chicago	IL	875	1000
Albany Park	Chicago	IL	1050	1250
Downtown	Memphis	TN	1000	850
Kensington	New York	NY	1350	1900
Kempsville	Virginia Beach	VA	1175	1225
Flatlands	New York	NY	1350	1450
University Heights	New York	NY	1025	1185
Richmond Hill	New York	NY	1350	1500
Encanto	Phoenix	AZ	845	850
Little Havana	Miami	FL	1250	1425
Northwest	Chula Vista	CA	1165	1295
Central City	Los Angeles	CA	\N	1500
Maspeth	New York	NY	1600	1700
Westwood	Los Angeles	CA	3250	3200
Queens Village	New York	NY	1400	1425
Flagami	Miami	FL	1250	1395
Lake Highlands	Dallas	TX	865	1029
Bedford Park	New York	NY	1100	1250
Hoover	Fresno	CA	755	735
Bay Ridge	New York	NY	1400	1650
Lake View	Chicago	IL	1500	1700
Mott Haven	New York	NY	1329	1800
Lone Mountain	Las Vegas	NV	1050	1150
Casas Adobes	Tucson	AZ	860	1250
Northeast Anaheim	Anaheim	CA	1545	1500
Englewood	Chicago	IL	1000	1000
Centennial Hills	Las Vegas	NV	1135	1100
Fairgrounds	San Jose	CA	1470	2161
Granada Hills	Los Angeles	CA	2075	2300
Gresham	Chicago	IL	775	775
Valencia	Santa Clarita	CA	1675	2000
Golfcrest - Bellfort - Reveille	Houston	TX	599	\N
Michael Way	Las Vegas	NV	771	900
Woodside	New York	NY	1450	1750
Mclane	Fresno	CA	685	750
Santa Teresa	San Jose	CA	1945	2240
Greater Uptown	Houston	TX	1399	1650
Highland Park	Los Angeles	CA	1190	1399
Bayside	New York	NY	1700	1900
Brighton Park	Chicago	IL	\N	800
Southwest	Arlington	TX	821	1250
Coney Island	New York	NY	1450	1600
Woodlake - Briarmeadow	Houston	TX	835	1335
Southwest Anaheim	Anaheim	CA	1290	1600
Central	El Paso	TX	\N	800
University City	San Diego	CA	1700	1845
Oak Lawn	Dallas	TX	1571	1502
Summerlin North	Las Vegas	NV	1250	1400
Hamilton Heights	New York	NY	1650	2200
Rancho Penasquitos	San Diego	CA	1575	2100
Fordham	New York	NY	975	1245
Winnetka	Los Angeles	CA	1795	1850
Sunnyside	New York	NY	1495	1785
Chelsea	New York	NY	2750	3474
Mid City West	Los Angeles	CA	2395	2500
Brighton	Boston	MA	1800	1995
Greenville	Jersey City	NJ	1175	1200
Alameda - West Flagler	Miami	FL	1350	1600
Memorial	Houston	TX	1195	2081
Woodland Hills	Los Angeles	CA	2495	2150
El Sereno	Los Angeles	CA	1600	1350
Greenwich Village	New York	NY	2750	3350
South Shore	Chicago	IL	792	750
Palms	Los Angeles	CA	1550	1795
Almaden Valley	San Jose	CA	\N	2495
Desert View	Phoenix	AZ	1500	1695
Gulfton	Houston	TX	830	985
Portage Park	Chicago	IL	800	1150
Briargate	Colorado Springs	CO	1150	1250
Richmond	Philadelphia	PA	700	825
Salem	Virginia Beach	VA	1250	1395
Rego Park	New York	NY	1425	1775
Carmel Valley	San Diego	CA	2010	2150
West Adams	Los Angeles	CA	\N	1275
Jefferson Park	Chicago	IL	1200	1100
Allapattah	Miami	FL	1400	1200
Kew Gardens Hills	New York	NY	1600	1625
Valley High-North Laguna	Sacramento	CA	1175	1250
Rancho Bernardo	San Diego	CA	1600	1695
Canyon Country	Santa Clarita	CA	1432	1655
Newhall	Santa Clarita	CA	1350	1550
Morris Heights	New York	NY	1175	1309
Anaheim Hills	Anaheim	CA	2005	2245
Humboldt Park	Chicago	IL	1000	1300
Bay Area	Corpus Christi	TX	754	1200
Morningside Heights	New York	NY	2300	2750
Ocean Parkway	New York	NY	1300	1495
Ocean Hill	New York	NY	1550	1800
Southeast Anaheim	Anaheim	CA	1295	1495
Montbello	Denver	CO	1050	1352
Greater Heights	Houston	TX	1500	1408
Parkchester	New York	NY	1050	1199
River Oaks-Kirby-Balmoral	Memphis	TN	850	1050
Oak Forest - Garden Oaks	Houston	TX	1300	1475
North Dallas	Dallas	TX	1042	1995
Frankford	Philadelphia	PA	685	725
East Boston	Boston	MA	1500	1800
Harbor Gateway	Los Angeles	CA	1095	1395
Parkway Village-Oakhaven	Memphis	TN	\N	850
Longwood	New York	NY	\N	1375
Mar Vista	Los Angeles	CA	1545	1875
Coral Way	Miami	FL	1575	2000
Back of the Yards	Chicago	IL	1075	1050
Watts	Los Angeles	CA	\N	1500
South End	Tacoma	WA	875	1100
Mid Wilshire	Los Angeles	CA	1950	1932
Bayside	Virginia Beach	VA	1150	1250
Briarforest Area	Houston	TX	794	1029
Lawncrest	Philadelphia	PA	815	725
North	Arlington	TX	599	900
High Bridge	New York	NY	1300	1200
Gage Park	Chicago	IL	810	\N
Studio City	Los Angeles	CA	2478	2000
North Ironbound	Newark	NJ	\N	1400
Greater Greenspoint	Houston	TX	499	750
Crenshaw	Los Angeles	CA	1375	925
Cragin	Chicago	IL	1100	975
North Cheyenne	Las Vegas	NV	1000	1095
Arleta	Los Angeles	CA	\N	\N
Bridgeport	Chicago	IL	900	950
Lake View East	Chicago	IL	1095	1250
Laveen	Phoenix	AZ	1049	1050
Norwood	New York	NY	1075	1275
Melrose	New York	NY	1325	1475
North Park	San Diego	CA	1125	1295
East Reno	Reno	NV	680	800
Edenvale - Seven Trees	San Jose	CA	1700	2295
Silver Lake	Los Angeles	CA	2400	1895
Morris Park	New York	NY	1200	1250
Green Valley North	Henderson	NV	948	1295
Inwood	New York	NY	1295	1450
Woodhaven	New York	NY	1250	1400
Charleston Heights	Las Vegas	NV	800	875
Venice	Los Angeles	CA	3900	3750
Kalihi-Palama	Honolulu	HI	\N	1595
Chatsworth	Los Angeles	CA	2100	2250
Berryessa	San Jose	CA	\N	2595
Wakefield	New York	NY	1450	1294
Westchester	Los Angeles	CA	1884	1900
Downtown	Los Angeles	CA	1695	2404
Dyker Heights	New York	NY	1500	1750
Hyde Park	Los Angeles	CA	\N	1275
South Loop	Chicago	IL	1800	1936
Addicks Park Ten	Houston	TX	900	1105
Shelby Forest-Frayser	Memphis	TN	525	650
East Tremont	New York	NY	1250	1500
Powers	Colorado Springs	CO	1150	1275
Hollis	New York	NY	1500	1511
Southwest	Reno	NV	850	850
Rancho Charleston	Las Vegas	NV	925	969
Co-op City	New York	NY	\N	\N
Brentwood	Los Angeles	CA	2300	3400
Mattapan	Boston	MA	1400	1675
West Lawn	Chicago	IL	\N	800
Wolf Creek	Dallas	TX	\N	1095
La Sierra	Riverside	CA	1361	1200
St. Albans	New York	NY	1436	1400
West	Fresno	CA	950	1025
Olney	Philadelphia	PA	\N	750
Berclair-Highland Heights	Memphis	TN	650	625
Southwest Colorado Springs	Colorado Springs	CO	860	1100
South Boston	Boston	MA	2295	2750
Riverview West	Santa Ana	CA	\N	1375
Lincoln Heights	Los Angeles	CA	\N	1250
Whitney	Las Vegas	NV	895	1000
Cobbs Creek	Philadelphia	PA	\N	850
Corona Valley	Corona	CA	2350	2350
Throggs Neck	New York	NY	1400	1700
Greater Inwood	Houston	TX	799	745
Holmesburg-Torresdale	Philadelphia	PA	1100	950
Mayfair	Philadelphia	PA	\N	900
East Las Vegas	Las Vegas	NV	700	725
Edgewater Beach	Chicago	IL	795	1050
Oak Cliff	Dallas	TX	1500	1008
West Hills	Los Angeles	CA	2500	2850
North Central	Pasadena	CA	1890	1750
Fort Greene	New York	NY	2400	2750
Fort Bend - Houston	Houston	TX	\N	1100
14621	Rochester	NY	\N	650
Del Rey	Los Angeles	CA	2740	3050
Bustleton	Philadelphia	PA	790	995
Northwest Anaheim	Anaheim	CA	1220	1600
Whitestone	New York	NY	1700	1875
Little Woods	New Orleans	LA	750	1200
Mears Corner	Virginia Beach	VA	1295	1400
Glendale	New York	NY	1400	1500
Hyde Park	Boston	MA	1400	1600
Old Brooklyn	Cleveland	OH	595	695
Middle Village	New York	NY	1500	1650
M Streets	Dallas	TX	1309	1325
Homecrest	New York	NY	1250	1450
West Raleigh	Raleigh	NC	750	1000
Kingsessing	Philadelphia	PA	800	795
Prospect Lefferts Gardens	New York	NY	1250	1600
South Corona	Corona	CA	\N	2200
Makiki-Lower Punchbowl-Tantalus	Honolulu	HI	1275	1150
Kingsbridge	New York	NY	1250	1300
Marquette Park	Chicago	IL	850	790
The Colony	Anaheim	CA	1339	1760
Hollywood Hills	Los Angeles	CA	3850	3799
Brighton Beach	New York	NY	1550	1725
Juniata Park-Feltonville	Philadelphia	PA	\N	749
Bronzeville	Chicago	IL	1065	1250
Greenpoint	New York	NY	2100	2700
West Oak Lane	Philadelphia	PA	\N	720
Torresdale	Philadelphia	PA	899	850
Otay Mesa West	San Diego	CA	\N	1400
Downtown	Jersey City	NJ	2050	2200
Gold  Coast	Chicago	IL	1575	1832
Rochdale	New York	NY	1600	1650
Belmont Central	Chicago	IL	\N	1200
Bay Terraces	San Diego	CA	1600	1700
Columbia Heights	Washington	DC	2275	2395
Somerton	Philadelphia	PA	825	795
Wynnefield	Philadelphia	PA	1200	1195
Hawaii Kai	Honolulu	HI	2600	2800
La Jolla	San Diego	CA	3950	5000
Sugar House	Salt Lake City	UT	899	900
Roslindale	Boston	MA	1350	1800
Poly High District	Long Beach	CA	925	1150
West Roxbury	Boston	MA	1650	1795
Sawtelle	Los Angeles	CA	1850	2195
Center City West	Philadelphia	PA	1750	1950
Saugus	Santa Clarita	CA	1525	1900
Summerlin South	Las Vegas	NV	1450	1638
Payne Phallen	Saint Paul	MN	825	1050
The Lakes	Las Vegas	NV	1195	1395
Clinton	New York	NY	2850	3100
Jefferson Park	Los Angeles	CA	1250	1300
Eastex - Jensen Area	Houston	TX	\N	1200
Pacific Beach	San Diego	CA	1550	2000
Tarzana	Los Angeles	CA	2400	1990
Capitol Hill	Seattle	WA	1525	1640
Spring Branch West	Houston	TX	999	1533
Valley Glen	Los Angeles	CA	1250	1595
South Chicago	Chicago	IL	950	900
West Pullman	Chicago	IL	1325	1150
Overbrook	Philadelphia	PA	825	800
Prospect Hill	San Antonio	TX	\N	\N
Roxborough	Philadelphia	PA	1155	1374
Westchase	Houston	TX	800	1233
Bellerose	New York	NY	1500	1550
Gateway - Green Valley Ranch	Denver	CO	965	1459
Westwood	Cincinnati	OH	535	699
Eastside-ENACT	Tacoma	WA	1195	1000
Financial District	New York	NY	3000	3345
Neartown - Montrose	Houston	TX	1352	1804
Alum Rock-East Foothills	San Jose	CA	\N	1980
South End	Boston	MA	2400	2900
Little Haiti	Miami	FL	1400	1495
West End	Tacoma	WA	875	925
Glassell Park	Los Angeles	CA	1200	1185
West Side	Long Beach	CA	\N	\N
Allston	Boston	MA	2200	2400
North Valleys	Reno	NV	950	1100
Flatiron District	New York	NY	2895	3600
Alexandria Wrest	Alexandria	VA	1503	1650
Southeast Boise	Boise	ID	795	975
Tierrasanta	San Diego	CA	1450	1845
Briarwood	New York	NY	1450	1475
Elmwood	Philadelphia	PA	700	785
Pico-Union	Los Angeles	CA	\N	850
Haddington-Carroll Park	Philadelphia	PA	800	825
Jamaica Plain	Boston	MA	1800	2400
Pennsport-Whitman-Queen	Philadelphia	PA	1150	1295
Rhawnhurst	Philadelphia	PA	825	875
Northeast	Anchorage	AK	\N	1575
Fairhill	Philadelphia	PA	\N	700
Northshore	Houston	TX	619	\N
Reynolds Corners	Toledo	OH	650	\N
Capitol Hill	Washington	DC	1800	2100
South Dallas	Dallas	TX	1250	1095
Fort Hamilton	New York	NY	1375	1695
Auburndale	New York	NY	1500	2000
Wharton-Hawthorne-Bella Vista	Philadelphia	PA	1350	1495
Brickell	Miami	FL	1900	2400
McCully-Moiliili	Honolulu	HI	1350	1200
Center City East	Philadelphia	PA	1395	1650
Wrigley	Long Beach	CA	995	1200
Garfield Ridge	Chicago	IL	\N	1600
Greater Eastside	Saint Paul	MN	795	775
North Dorchester	Boston	MA	1725	1995
Spring Branch Central	Houston	TX	899	\N
Journal Square	Jersey City	NJ	1300	1450
Eagle Rock	Los Angeles	CA	\N	1495
Los Feliz	Los Angeles	CA	1724	2150
Indian River	Chesapeake	VA	1220	1200
Ravenswood	Chicago	IL	975	1400
Eagle Ford	Dallas	TX	\N	\N
Nevada-Lidgerwood	Spokane	WA	660	625
North Linden	Columbus	OH	595	650
Howard Beach	New York	NY	1650	2000
North Austin	Austin	TX	725	895
Pocket	Sacramento	CA	999	1295
Harvard Heights	Los Angeles	CA	\N	1325
Washington Avenue Coalition - Memorial Park	Houston	TX	1634	2015
West Englewood	Chicago	IL	1200	1200
Meadowview	Sacramento	CA	1100	1100
Northwest Colorado Springs	Colorado Springs	CO	955	1100
Forest Park	Springfield	MA	990	950
Northside Village	Houston	TX	\N	\N
Academy Gardens	Philadelphia	PA	950	875
Bernal Heights	San Francisco	CA	3200	2489
Aliamanu-Salt Lake-Foster Village	Honolulu	HI	1390	1400
University District	Seattle	WA	1199	1415
College Point	New York	NY	1600	1700
Paradise Hills	Albuquerque	NM	\N	1150
Spring Branch East	Houston	TX	1250	1450
Clairemont Mesa East	San Diego	CA	1234	1475
West Valley	Boise	ID	795	945
Laurelton	New York	NY	1500	1600
Westgate Hts	Albuquerque	NM	\N	995
Ramona	Riverside	CA	985	1050
North End	Saint Paul	MN	750	1050
Highland Hills	San Antonio	TX	\N	730
Acres Home	Houston	TX	815	745
South Boulevard-Park Row Historic	Dallas	TX	\N	1250
South Natomas	Sacramento	CA	803	1195
Landmark-Van Dom	Alexandria	VA	1499	1660
San Ysidro	San Diego	CA	\N	\N
Waikiki	Honolulu	HI	1397	1850
University City	Philadelphia	PA	1438	895
Abbott Loop	Anchorage	AK	\N	1350
Rosedale	New York	NY	1650	1700
Winchester	Las Vegas	NV	825	950
South Tacoma	Tacoma	WA	760	1000
Urbandale-Parkdale	Dallas	TX	\N	950
Pelham Bay	New York	NY	1300	1600
Creston	Grand Rapids	MI	750	795
Ogontz	Philadelphia	PA	\N	850
Northwest	Reno	NV	1275	1425
Woodbridge	Irvine	CA	1950	2500
Great Bridge	Chesapeake	VA	1375	1450
Douglaston-Little Neck	New York	NY	1800	2050
Greenwood	New York	NY	1750	2150
Highland	Saint Paul	MN	1175	1125
Echo Park	Los Angeles	CA	\N	1580
North End	Tacoma	WA	995	995
Marine Park	New York	NY	\N	1400
Northeast	Reno	NV	695	625
Great Neck	Virginia Beach	VA	1179	1195
South Central	Reno	NV	685	600
Central	Arlington	TX	811	720
Capitol	Town of Madison	WI	1250	1250
Excelsior	San Francisco	CA	\N	\N
North Central	Philadelphia	PA	1350	1600
Powellhurst Gilbert	Portland	OR	770	929
Meadowbrook - Allendale	Houston	TX	\N	\N
East Toledo	Toledo	OH	\N	485
Columbus Circle	New York	NY	2850	3250
Point Breeze	Philadelphia	PA	975	950
Harbor City	Los Angeles	CA	1790	1350
Las Tierras	El Paso	TX	\N	1100
Pelham Gardens	New York	NY	1350	1400
West Village	New York	NY	2850	3745
South Norfolk	Chesapeake	VA	975	1150
Oakland Gardens	New York	NY	1500	1850
West Town	Chicago	IL	1500	2110
Fresh Meadows	New York	NY	1700	1750
North Austin	Chicago	IL	900	825
South Philadelphia	Philadelphia	PA	875	1000
Kew Gardens	New York	NY	1420	1650
Liliha-Kapalama	Honolulu	HI	\N	1000
Central Richmond	San Francisco	CA	1795	2650
Save the Valley 21	El Paso	TX	\N	\N
Springlake, University Terrace	Shreveport	LA	815	1050
Otay Ranch	Chula Vista	CA	2195	2095
Eltingville	New York	NY	\N	1900
Clinton Hill	New York	NY	1800	2650
Great Kills	New York	NY	\N	1350
Edison	Fresno	CA	\N	650
Potomac West	Alexandria	VA	1910	2155
Fenway	Boston	MA	2050	2500
Linda Vista	San Diego	CA	1526	1750
Greater Hobby Area	Houston	TX	439	\N
Pacific Palisades	Los Angeles	CA	5000	5000
Disston Heights	Saint Petersburg	FL	950	1100
Forest Hill	Newark	NJ	\N	1200
Hunting Park	Philadelphia	PA	\N	725
Sand Lake	Anchorage	AK	\N	1650
Liberty City	Miami	FL	1100	995
Manoa	Honolulu	HI	2200	1300
Hazelwood	Portland	OR	825	825
Uptown	Chicago	IL	1150	1255
Fox Chase	Philadelphia	PA	\N	775
Sixteen Acres	Springfield	MA	\N	\N
Germantown	Philadelphia	PA	775	850
Arlanza	Riverside	CA	\N	1325
Greenbrier East	Chesapeake	VA	1295	1395
Northwest	Spokane	WA	\N	750
Valley Village	Los Angeles	CA	1900	1685
Centennial	Portland	OR	850	1000
Active Bethel	Eugene	OR	825	850
Sunland	Los Angeles	CA	1095	2199
South	Pasadena	CA	1809	1937
Fairmount-Spring Garden	Philadelphia	PA	1488	1375
West Park	Irvine	CA	2100	2085
Pico-Robertson	Los Angeles	CA	1995	2095
West Side	Jersey City	NJ	1550	1300
Northampton	Hampton	VA	925	1100
Serra Mesa	San Diego	CA	2000	1795
Logan-Fern Rock	Philadelphia	PA	\N	800
East Germantown	Philadelphia	PA	850	715
East Central	Salt Lake City	UT	\N	800
Anthem	Henderson	NV	1350	1450
Sutton Place	New York	NY	2700	3400
Tujunga	Los Angeles	CA	1285	1500
Near North	Chicago	IL	1575	1984
Girard Estates	Philadelphia	PA	900	950
South Park	Houston	TX	\N	900
Bayview	San Francisco	CA	\N	2200
Westbury	Houston	TX	1200	800
Brooklyn Heights	New York	NY	2175	2750
West Central	Pasadena	CA	1900	1695
South Side	Toledo	OH	450	695
Weequahic	Newark	NJ	\N	1175
Green Valley South	Henderson	NV	1300	1225
Flour Bluff	Corpus Christi	TX	\N	1150
Seminary Hill	Alexandria	VA	1550	1595
Downtown	San Francisco	CA	1395	3300
Lower Peters Canyon	Irvine	CA	2495	1905
19th Ward	Rochester	NY	\N	695
Castle Hill	New York	NY	1200	1600
West Las Vegas	Las Vegas	NV	895	850
East Garfield Park	Chicago	IL	1200	1100
Back Bay	Boston	MA	2500	2850
Porter Ranch	Los Angeles	CA	2645	2795
Mission Hills	Los Angeles	CA	\N	1895
Roseland	Chicago	IL	700	850
Northwest Torrance	Torrance	CA	1275	1525
Braeswood Place	Houston	TX	1227	1579
East Central	Pasadena	CA	1095	1900
East Side	Chicago	IL	\N	720
Cilo Vista	El Paso	TX	859	975
Sunnyside	Houston	TX	\N	874
Central	Tacoma	WA	1000	1095
South of Market	San Francisco	CA	3000	3405
Northwood	Irvine	CA	1995	2240
Hermosa	Chicago	IL	975	900
Central Sunset	San Francisco	CA	2300	2990
Five Points	Toledo	OH	\N	725
Belmont	New York	NY	1380	1250
Five Oaks - Triple Creek	Beaverton	OR	925	930
Old Northwest - West University	Reno	NV	995	1050
Hellman	Long Beach	CA	1000	1050
Orangecrest	Riverside	CA	\N	1950
Meyerland Area	Houston	TX	1055	1693
Central City East	Los Angeles	CA	2150	2070
University	Riverside	CA	945	1100
South Reno	Reno	NV	1150	1450
Greater Fifth Ward	Houston	TX	\N	850
Poplar-Ludlow-Yorktowne	Philadelphia	PA	1295	1500
Westwood	Houston	TX	\N	\N
Deep Creek North	Chesapeake	VA	1225	1200
Bergen-Lafayette	Jersey City	NJ	1250	1200
Battle Creek	Saint Paul	MN	795	1150
Alleghany West	Philadelphia	PA	1120	1000
North San Jose	San Jose	CA	1925	2416
Scripps Ranch	San Diego	CA	1800	1900
Edgebrook Area	Houston	TX	569	725
Strawberry Mansion	Philadelphia	PA	1400	800
Diamond Head-Kapahulu-St. Louis	Honolulu	HI	3200	3200
Tenderloin	San Francisco	CA	1195	1825
Visitacion Valley	San Francisco	CA	\N	\N
Lents	Portland	OR	865	975
People Active in Community Effort	San Antonio	TX	\N	875
Ottawa	Toledo	OH	\N	550
Sheep Mountain	Las Vegas	NV	1295	1300
Greenway - Upper Kirby Area	Houston	TX	1399	1760
Spring Branch North	Houston	TX	680	1375
Hampden	Denver	CO	796	838
Ost - South Union	Houston	TX	\N	1195
West Brighton	New York	NY	\N	1500
Cal Young	Eugene	OR	980	956
Cedarbrook	Philadelphia	PA	675	850
Wynwood - Edgewater	Miami	FL	1675	2150
Taylor Ranch	Albuquerque	NM	745	1050
Elkhorn	Omaha	NE	\N	1170
Heartland Village	New York	NY	\N	1500
Wingate	New York	NY	1200	1750
Clearview	New York	NY	1900	2175
Macalester-Groveland	Saint Paul	MN	895	850
West Price HIll	Cincinnati	OH	490	650
Okolona	Louisville	KY	\N	\N
East Little York - Homestead	Houston	TX	\N	900
Westgate	Henderson	NV	1250	1495
Greenbrier West	Chesapeake	VA	1195	1300
Goodyear Heights	Akron	OH	\N	\N
Kings Grant	Virginia Beach	VA	1725	1350
Unionport	New York	NY	1125	1300
The Plaza	Long Beach	CA	\N	1975
East Tampa	Tampa	FL	587	875
Chatham	Chicago	IL	1000	690
Midtown	New York	NY	2700	3395
McGinley Square	Jersey City	NJ	1395	1650
Braeburn	Houston	TX	567	\N
Warrendale	Detroit	MI	\N	700
Turtle Bay	New York	NY	2795	3050
Tule Springs	Las Vegas	NV	1295	1250
Southwest Raleigh	Raleigh	NC	875	1090
Weston Ranch	Stockton	CA	1295	1295
Parkside	San Francisco	CA	\N	2195
Harder-Tennyson	Hayward	CA	1200	1375
Sunrise	Las Vegas	NV	720	800
North Aurora	Aurora	CO	\N	725
Western Branch North	Chesapeake	VA	1100	1295
Merrlam Park	Saint Paul	MN	1250	1300
Petworth	Washington	DC	2200	1800
Pacific Heights	San Francisco	CA	2500	3900
Kaimuki	Honolulu	HI	\N	\N
Hyde Park	Chicago	IL	935	1160
Port Richmond	New York	NY	\N	2300
South Acres - Crestmont Park	Houston	TX	\N	1000
East Mount Airy	Philadelphia	PA	850	855
Summerfields	Fort Worth	TX	\N	1150
Heart of Chicago	Chicago	IL	1050	975
Nob Hill	San Francisco	CA	1995	3200
Tioga-Nicetown	Philadelphia	PA	800	685
West Elsdon	Chicago	IL	\N	\N
Greater Pinellas Point	Saint Petersburg	FL	785	1200
Prosperity Church Road	Charlotte	NC	885	1105
Chicago Lawn	Chicago	IL	650	710
Jefferson	Cleveland	OH	\N	775
Beach Haven	Jacksonville	FL	975	1200
Kamm's Corner	Cleveland	OH	\N	\N
Bucktown	Chicago	IL	1800	2200
Point Loma Heights	San Diego	CA	1650	1445
Sandalwood	Jacksonville	FL	1000	1275
Golden Glades - The Woods	Jacksonville	FL	1044	1300
Astrodome Area	Houston	TX	1110	1243
Broadmoor, Anderson Island, Shreve Isle.	Shreveport	LA	745	1000
Frankford	Baltimore	MD	\N	1200
East Houston	Houston	TX	\N	1250
Downtown	Stamford	CT	1925	1975
Magnolia	Seattle	WA	1095	1500
Maplewood	Rochester	NY	\N	695
Nuuanu-Punchbowl	Honolulu	HI	\N	2000
Parkway	Sacramento	CA	1025	1095
Mount Washington	Los Angeles	CA	\N	2000
Byberry	Philadelphia	PA	\N	\N
East Sacramento	Sacramento	CA	\N	1150
Metro West	Orlando	FL	900	975
Alderwood Manor	Lynnwood	WA	1150	\N
Forest Park East	Columbus	OH	589	\N
DeVeaux	Toledo	OH	\N	750
Gowanus	New York	NY	2000	3000
Avondale	Chicago	IL	1275	1650
Ala Moana-Kakaako	Honolulu	HI	3000	3000
East Arlington	Jacksonville	FL	1200	1395
Kenmore	Boston	MA	2100	2100
Trinity - Houston Gardens	Houston	TX	\N	\N
Citrus Grove	Glendale	CA	1500	1325
Inner Richmond	San Francisco	CA	2000	3000
Buffalo	Las Vegas	NV	1000	800
Prospect Heights	New York	NY	1600	2550
DRNAG	San Bernardino	CA	850	1150
Dayton's Bluff	Saint Paul	MN	1099	995
Old Colorado City	Colorado Springs	CO	795	1000
South Weymouth	Weymouth	MA	\N	1409
Manhattanville	New York	NY	1595	1900
Lake Murray	San Diego	CA	\N	1645
Southeast Raleigh	Raleigh	NC	1050	1100
West Farms	New York	NY	\N	1500
Mission Hill	Boston	MA	3050	3500
Noe Valley	San Francisco	CA	3000	3900
Pecan Park	Houston	TX	\N	\N
New Utrecht	New York	NY	1375	1400
Kuliouou-Kalani Iki	Honolulu	HI	5000	4000
Vance Jackson	San Antonio	TX	784	895
Morgan Park	Chicago	IL	\N	1150
Mount Greenwood	Chicago	IL	\N	\N
Mt Pleasant	Cleveland	OH	\N	550
Northeast Tacoma	Tacoma	WA	948	1375
Old Aurora	New Orleans	LA	690	1200
Outer Sunset	San Francisco	CA	\N	1995
Portola	San Francisco	CA	\N	1600
Downtown	Houston	TX	1372	2085
Midtown	Atlanta	GA	1299	1519
Great Bridge East	Chesapeake	VA	\N	1900
North Collinwood	Cleveland	OH	\N	550
Ellet	Akron	OH	\N	\N
Charlestown	Boston	MA	2750	2600
Eastside	Riverside	CA	1250	885
Upper Roseville	Newark	NJ	\N	1300
Paradise Hills	San Diego	CA	\N	1850
Logan Circle	Washington	DC	2575	2790
Grays Ferry	Philadelphia	PA	750	790
West Grand	Grand Rapids	MI	\N	750
Greater Avenues	Salt Lake City	UT	990	1000
Fairbanks - Northwest Crossing	Houston	TX	670	845
Cedar Park	Philadelphia	PA	850	900
Adams Morgan	Washington	DC	1699	2500
Outer Richmond	San Francisco	CA	\N	2700
West Akron	Akron	OH	\N	\N
Bay View	Milwaukee	WI	\N	765
Inner Sunset	San Francisco	CA	\N	3000
Tampa Palms	Tampa	FL	967	1295
Hyde Park Brookwood, Southern Hills	Shreveport	LA	\N	\N
Puritas-Longmead	Cleveland	OH	\N	675
Tribeca	New York	NY	2500	4650
Upper Clinton Hill	Newark	NJ	\N	1200
Seatack	Virginia Beach	VA	1129	1250
Kenmore	Akron	OH	\N	650
Whitmer - Trilby	Toledo	OH	\N	610
Huntridge	Las Vegas	NV	899	950
Montclare	Chicago	IL	\N	1350
University Village - Little Italy	Chicago	IL	1600	1800
Washington Highlands	Washington	DC	995	\N
Fishtown	Philadelphia	PA	1650	1695
Summit-University	Saint Paul	MN	900	1195
South Broadway	Cleveland	OH	\N	600
Franklin Park	Austin	TX	740	\N
Martha Lake	Lynnwood	WA	\N	\N
Greenwood	Seattle	WA	1450	1345
Midvale Park	Tucson	AZ	\N	925
Encanto	San Diego	CA	\N	1900
Blueberry Hill-Brigadoon-Stoneybrook-Baralto	Lexington	KY	645	799
Glenville	Cleveland	OH	\N	\N
Audubon	New Orleans	LA	\N	2200
Harrowgate	Philadelphia	PA	\N	675
The Waterfront	Jersey City	NJ	2685	3000
Playa Del Rey	Los Angeles	CA	2228	2350
West End	Providence	RI	895	1250
Liberty Heights	Springfield	MA	\N	925
Montavilla	Portland	OR	\N	850
Baychester	New York	NY	\N	1700
Wallingford	Seattle	WA	\N	1795
Bay Park	San Diego	CA	1265	1860
Buckroe	Hampton	VA	900	930
Clearing (W)	Chicago	IL	\N	1175
Belaire-Edison	Baltimore	MD	1100	1200
CUF	Cincinnati	OH	595	1000
West Boulevard	Cleveland	OH	\N	800
Macgregor	Houston	TX	1450	1654
Central West End	Saint Louis	MO	830	995
Franklin Park	Toledo	OH	\N	\N
Tudor City	New York	NY	2695	2900
University Place	Houston	TX	1470	2033
Canyon Crest	Riverside	CA	1450	1560
Mantua	Philadelphia	PA	1100	1100
Ardenwood	Fremont	CA	\N	2500
Westwood	Denver	CO	\N	\N
Upper Vailsburg	Newark	NJ	1950	1150
Mariposa	Glendale	CA	\N	\N
Desert Shores	Las Vegas	NV	800	1250
Cultural Corridor	Las Vegas	NV	850	550
Park Manor	Chicago	IL	1000	850
Anaheim Resort	Anaheim	CA	1395	1550
Mountain View	San Diego	CA	\N	1100
Dutchtown	Saint Louis	MO	550	550
O'Hare	Chicago	IL	1500	1065
Arlington Heights	Los Angeles	CA	\N	1795
Wedgwood	Fort Worth	TX	\N	995
West University	Austin	TX	1295	1550
West Garfield Park	Chicago	IL	1295	853
Carnegie Hill	New York	NY	2650	3199
Green Valley Ranch	Henderson	NV	1295	1575
Central	Fresno	CA	950	495
Barry Square	Hartford	CT	725	875
Stuyvesant Town	New York	NY	\N	3275
Iah - Airport Area	Houston	TX	\N	\N
West Side	Newark	NJ	\N	1200
Centerville	Fremont	CA	1250	1520
El Camino Real	Irvine	CA	2350	2350
Morningside	Detroit	MI	800	750
Sun Lakes	Chandler	AZ	1300	1500
Squirrel Hill South	Pittsburgh	PA	1570	1395
Lower Vailsburg	Newark	NJ	\N	\N
Oleander Sunset	Bakersfield	CA	\N	750
Spuyten Duyvil	New York	NY	1870	2050
Rita Ranch	Tucson	AZ	1050	1050
West Side	Saint Paul	MN	\N	1200
Gandy-Sun Bay South	Tampa	FL	874	1150
Northwest	Corpus Christi	TX	\N	1200
Garfield Park	Grand Rapids	MI	\N	750
East Side	Long Beach	CA	1075	1150
Southwest Detroit	Detroit	MI	\N	\N
West Colorado Springs	Colorado Springs	CO	950	950
Nestor	San Diego	CA	\N	1600
Thomas Dale	Saint Paul	MN	1050	895
Galewood	Chicago	IL	\N	1300
Alamitos Beach	Long Beach	CA	1395	1300
Eastwick	Philadelphia	PA	\N	900
Traffic Circle	Long Beach	CA	1535	1620
Chambersburg	Trenton	NJ	900	1062
Windsor Park	Austin	TX	749	1075
Logan Heights	San Diego	CA	\N	1195
East Weymouth	Weymouth	MA	1124	1415
Capitol Hill	Denver	CO	975	1020
Mid-City	New Orleans	LA	1175	975
Downtown	Fremont	CA	1717	2051
East Oak Lane	Philadelphia	PA	\N	775
Flamingo Lummus	Miami Beach	FL	\N	1900
New Tacoma	Tacoma	WA	895	1000
Delmar Parkway	Aurora	CO	\N	800
Pioneer Park	Las Vegas	NV	825	995
Bluffview	Dallas	TX	1250	1340
Dupont Circle	Washington	DC	2250	2520
Poplar Grove	Salt Lake City	UT	\N	895
Southside	Columbus	OH	\N	945
North Stamford	Stamford	CT	3900	4000
North Park	Buffalo	NY	\N	775
Cambria Heights	New York	NY	1550	2500
Lake Houston	Houston	TX	819	2000
Sixteenth Street Heights	Washington	DC	1895	2100
Outer Parkside	San Francisco	CA	\N	\N
Central Beaverton	Beaverton	OR	825	1100
Westchester Heights	New York	NY	1244	1300
Detroit Shoreway	Cleveland	OH	\N	635
Lincoln Park	Chicago	IL	1550	1735
Oak Park	San Diego	CA	\N	1378
Citizens Southwest	Jackson	MS	675	750
Hampden South	Denver	CO	1060	1042
Weber Ranch	Stockton	CA	1250	1305
Hill	New Haven	CT	1000	1200
Wissinoming	Philadelphia	PA	\N	750
Fair Haven	New Haven	CT	1180	1100
Hartranft	Philadelphia	PA	1350	2000
Villages of Palm Beach Lakes	West Palm Beach	FL	1000	1200
Greater Third Ward	Houston	TX	\N	1450
Woodlawn	Chicago	IL	1200	1125
Zaferia	Long Beach	CA	1250	1095
North Gateway	Phoenix	AZ	1345	1400
Finn Hill	Kirkland	WA	1675	1725
Russian Hill	San Francisco	CA	3095	4600
Firestone Park	Akron	OH	\N	725
Van Nest	New York	NY	1125	1400
Kensington	Philadelphia	PA	1000	1200
Creekside - Wagner	Stockton	CA	895	800
La Grange	Toledo	OH	\N	625
The Groves	Mesa	AZ	635	699
St.Johns	Portland	OR	\N	945
Lincoln Heights	Spokane	WA	\N	650
Mariner's Harbor	New York	NY	\N	1930
Hillcrest	San Diego	CA	1250	1600
Ceder Grove, Lynbrook	Shreveport	LA	\N	\N
Washington Square	Syracuse	NY	\N	700
North Clairemont	San Diego	CA	\N	\N
Central Weymouth	Weymouth	MA	\N	1406
West Humboldt Park	Chicago	IL	850	975
Near West Side	Chicago	IL	1600	1999
Irving Park	Chicago	IL	1100	1250
North Center	Chicago	IL	1300	1750
Chimney Lakes	Jacksonville	FL	1050	1195
Eastwood	Syracuse	NY	\N	575
Upper Eastside	Miami	FL	1300	1800
Shadyside	Pittsburgh	PA	1200	1295
Hillcrest	New York	NY	1750	2200
Alamo Farmsteads-Babcock Road	San Antonio	TX	964	1030
Georgetown	Washington	DC	5000	3250
Beverly Glen	Los Angeles	CA	9500	8950
Western Branch South	Chesapeake	VA	1400	1395
Downtown	Miami	FL	2050	2450
Album Park	El Paso	TX	\N	925
East Broad	Columbus	OH	760	1125
Second Ward	Houston	TX	\N	1566
Diamond Hill - Jarvis	Fort Worth	TX	\N	\N
Lee Miles	Cleveland	OH	\N	\N
Afton Oaks - River Oaks Area	Houston	TX	1260	1660
Magnolia Center	Riverside	CA	1095	1250
Downtown	Hampton	VA	845	995
Arden Heights	New York	NY	\N	1600
Greater Wythe	Hampton	VA	900	1050
Aberdeen	Hampton	VA	1055	995
Valley View	Henderson	NV	950	950
Miramar Ranch North	San Diego	CA	\N	2150
Somerset	Bellevue	WA	2290	2550
The Fan	Richmond	VA	795	1150
Northern Woods	Columbus	OH	609	\N
Cherryland	Hayward	CA	\N	\N
North Hill	Akron	OH	\N	\N
Ashburn	Chicago	IL	\N	\N
Rock Creek	Little Rock	AR	730	\N
Provincetowne	Charlotte	NC	1150	1400
Bixby Area	Long Beach	CA	\N	1245
Eastside	Santa Ana	CA	\N	\N
Sunnyside	Tucson	AZ	\N	625
Whittier	Minneapolis	MN	740	900
Riverdale	New York	NY	1695	1995
Palolo	Honolulu	HI	\N	\N
North King St	Hampton	VA	925	995
Willow Meadows - Willowbend Area	Houston	TX	695	1500
Bayshore-Klatt	Anchorage	AK	\N	1375
North Beach	Jacksonville	FL	795	850
Northwest	Portland	OR	985	1050
Lea Hill	Auburn	WA	1045	1375
McKinley Park	Chicago	IL	\N	950
City Center	Glendale	CA	1650	2332
MacDonald Ranch	Henderson	NV	1100	1395
College Hill	Cincinnati	OH	795	600
Cove - East Side	Stamford	CT	1600	1600
John Barrow	Little Rock	AR	\N	650
South Land Park	Sacramento	CA	\N	1000
Hayes Valley	San Francisco	CA	\N	3335
Downtown	Atlanta	GA	1100	1300
Belmont Gardens	Chicago	IL	1200	950
Independence Heights	Houston	TX	\N	\N
Lazy Brook - Timbergrove	Houston	TX	975	1205
Tacony	Philadelphia	PA	\N	650
Rockaway Park	New York	NY	1350	1300
Beverly	Chicago	IL	\N	1100
The Ohio State University	Columbus	OH	\N	800
McCullough Hills	Henderson	NV	1141	1375
Front Park	Buffalo	NY	\N	1000
Emerson Hill	New York	NY	\N	1700
Caddo Heights, South Highlands	Shreveport	LA	\N	660
Downtown	Honolulu	HI	1850	1575
Cheviot Hills	Los Angeles	CA	2900	3152
Cully	Portland	OR	745	1150
West Oak Hill	Austin	TX	1200	1300
Dobson Ranch	Mesa	AZ	799	1150
Downtown	Long Beach	CA	2000	1750
Windy Hill	Jacksonville	FL	1015	1020
Brookline	Pittsburgh	PA	\N	795
Belair	Augusta	GA	826	900
Jamaica Estates	New York	NY	1295	1549
East Oak Hill	Austin	TX	979	1305
Brainerd	Chicago	IL	\N	850
Rose Garden	San Jose	CA	\N	\N
Lakeview Terrace	Los Angeles	CA	\N	\N
Southwest	Wichita	KS	\N	725
Marina	San Francisco	CA	2500	3950
Northeast Torrance	Torrance	CA	\N	\N
Foggy Bottom	Washington	DC	1850	1900
Highland Creek	Charlotte	NC	1250	1325
Dellview Area	San Antonio	TX	\N	900
Brentwood-Darlington	Portland	OR	\N	1025
Pinnacle Peak	Scottsdale	AZ	3000	3000
North Riverdale	New York	NY	1895	1700
Washington Virginia Vale	Denver	CO	763	900
Springfield-Belmont	Newark	NJ	\N	\N
Hough	Cleveland	OH	\N	\N
City College Area	Long Beach	CA	\N	\N
Glen Eden	Hayward	CA	\N	\N
Springwells	Detroit	MI	\N	\N
Glendale	Salt Lake City	UT	\N	\N
Lawndale - Wayside	Houston	TX	\N	\N
Mid-Cambridge	Cambridge	MA	1850	2395
West Side	Stamford	CT	1425	1600
Glenbrook	Stamford	CT	1650	1700
South Lakes Dr - Soapstone Dr	Reston	VA	1450	1695
Angel Park Lindell	Las Vegas	NV	890	995
Bevo Mill	Saint Louis	MO	\N	650
Jacksonville Heights	Jacksonville	FL	750	875
Tower Grove South	Saint Louis	MO	595	625
Pine Hills	Albany	NY	\N	952
Calallen	Corpus Christi	TX	\N	\N
Jamaica Hills	New York	NY	1450	1400
River Mountain	Little Rock	AR	825	995
Belmont Heights	Chicago	IL	\N	1850
Lake Hills	Bellevue	WA	1750	1530
San Carlos	San Diego	CA	1400	1700
Beacon Hill	Seattle	WA	\N	\N
Virginia Village	Denver	CO	610	899
Hyde Park	Cincinnati	OH	725	1095
Van Ness - Civic Center	San Francisco	CA	2100	3700
Riverside Park	Buffalo	NY	\N	\N
Harlow	Eugene	OR	\N	855
Floral park	New York	NY	1600	1600
Pilsen	Chicago	IL	1355	1495
Yorkshire	Charlotte	NC	905	1100
Terrace Park	Tampa	FL	605	925
Five Points	Denver	CO	1420	1700
Gibson Springs	Henderson	NV	995	1275
Glen Oaks	New York	NY	1300	1700
Silver Spring	Milwaukee	WI	\N	\N
Riverside	Cambridge	MA	2250	2400
Pleasant Valley	Austin	TX	699	860
Oakwood	New York	NY	\N	1150
Mar Lee	Denver	CO	\N	795
Taku-Campbell	Anchorage	AK	\N	1650
Hillsborough	Raleigh	NC	1050	1300
Silverlake	Providence	RI	\N	\N
New Springville	New York	NY	\N	1300
Buckeye Shaker	Cleveland	OH	695	625
Tall Timbers-Brechtel	New Orleans	LA	757	700
Ocean Beach	San Diego	CA	1300	1500
South End	Hartford	CT	\N	825
West Los Angeles	Los Angeles	CA	2650	2495
Downtown	Las Vegas	NV	575	825
South Southwest	San Antonio	TX	\N	\N
West Mount Airy	Philadelphia	PA	1295	1025
Downtown	Bellevue	WA	1595	1875
Westside Connection	Grand Rapids	MI	\N	\N
East Price Hill	Cincinnati	OH	700	695
Belmont Heights	Long Beach	CA	1295	1650
Harambee	Milwaukee	WI	\N	650
Arverne	New York	NY	1650	1650
Chisholm Creek	Wichita	KS	550	925
Chevy Chase	Washington	DC	2060	1550
Carroll Gardens	New York	NY	2150	2950
Willmore City	Long Beach	CA	1050	950
Cambridgeport	Cambridge	MA	2465	2850
Windsor	Denver	CO	995	950
Highland, Stoner Hill	Shreveport	LA	\N	700
Sun City Summerlin	Las Vegas	NV	1195	1295
Stockton Metropolitan Airport	Stockton	CA	\N	1100
Heritage	San Antonio	TX	\N	995
Atwater Village	Los Angeles	CA	1500	1650
Park West	Chicago	IL	1150	1425
Spenard	Anchorage	AK	\N	925
Bay Ho	San Diego	CA	\N	2200
Downtown	Portland	OR	1375	1400
North Cambridge	Cambridge	MA	2077	2482
Lowry Park Central	Tampa	FL	700	980
Fairmuont	Newark	NJ	\N	1200
Palm Heights	San Antonio	TX	\N	\N
Turn of River	Stamford	CT	2200	2500
Hidden Valley	Charlotte	NC	695	810
Thalia	Virginia Beach	VA	1259	1250
Tennyson-Alquire	Hayward	CA	\N	\N
North Hill	Spokane	WA	\N	695
East Akron	Akron	OH	\N	650
University Heights	San Diego	CA	945	1250
Fremont	Seattle	WA	1800	1495
Calumet Heights	Chicago	IL	\N	820
Brookside	Tulsa	OK	\N	995
South Broad Street	Newark	NJ	\N	1325
Glenmoor	Fremont	CA	1395	\N
Hunts Point	New York	NY	\N	1309
Wanskuck	Providence	RI	725	800
Schuylkill Southwest	Philadelphia	PA	1450	1500
Northgate	Fremont	CA	\N	1570
Point Place	Toledo	OH	\N	\N
Magruder Area	Hampton	VA	1095	1175
Como	Saint Paul	MN	960	925
Southwyck	Toledo	OH	564	450
Great Northwest	San Antonio	TX	895	1075
Seventh Avenue	Newark	NJ	\N	\N
Midway	Saint Paul	MN	1300	1250
Overlake	Bellevue	WA	1125	1444
South Beach	San Francisco	CA	3295	4100
Millenia	Orlando	FL	900	1025
Riverwest	Milwaukee	WI	1150	850
Windsor Park	Charlotte	NC	695	850
Ballston-Virginia Square	Arlington	VA	2275	2400
Harvey Park	Denver	CO	\N	775
Amber Hills	San Bernardino	CA	\N	750
Russian Jack Park	Anchorage	AK	\N	1300
Grandview	Glendale	CA	1300	1495
Historic Mitchell Street	Milwaukee	WI	\N	\N
University	Stockton	CA	750	725
North-East Coconut Grove	Miami	FL	2200	2450
Del Rio	Jacksonville	FL	1050	1200
Ravenna	Seattle	WA	\N	1675
Northwest Akron	Akron	OH	\N	\N
Shenandoah	Miami	FL	1575	1850
Mercury Central	Hampton	VA	980	880
Old Irving Park	Chicago	IL	900	1100
Manayunk	Philadelphia	PA	1500	1595
Kyle Canyon	Las Vegas	NV	1050	1175
Edgewater	Chicago	IL	1050	935
Norwood Park East	Chicago	IL	\N	1200
Riverside	Austin	TX	780	1120
Boerum Hill	New York	NY	2350	2800
Park Glen	Fort Worth	TX	\N	1395
East Central	Spokane	WA	\N	795
Bagley	Detroit	MI	\N	800
East Forest	Charlotte	NC	695	\N
Reed Park	Mesa	AZ	\N	750
Phoebus	Hampton	VA	895	960
La Sierra South	Riverside	CA	\N	1649
Lower East Side	Milwaukee	WI	1400	1350
Logan	Spokane	WA	\N	575
Corlett	Cleveland	OH	\N	650
North Beacon Hill	Seattle	WA	\N	1099
Shawnee	Louisville	KY	\N	750
Greater Eastwood	Houston	TX	\N	\N
Richmond	Portland	OR	\N	1445
Southeast	Eugene	OR	\N	925
Mandarin Station - Losco	Jacksonville	FL	895	1295
Riviera	Redondo Beach	CA	\N	3380
Allied Gardens	San Diego	CA	\N	1600
Grand Crossing	Chicago	IL	750	950
First Hill	Seattle	WA	1299	1550
Corona Hills	Corona	CA	\N	1775
Norteast Citizens Action	Grand Rapids	MI	\N	\N
Lower Pacific Heights	San Francisco	CA	2300	2895
Marston	Denver	CO	875	1150
Sundale	Fremont	CA	1270	\N
Pleasant Valley	Portland	OR	\N	1230
McKinley Park	Stockton	CA	\N	\N
Sulphur Springs	Tampa	FL	\N	895
Buena Park	Chicago	IL	1050	1150
Airport	Honolulu	HI	\N	\N
Squirrel Hill North	Pittsburgh	PA	\N	1520
Mount Pleasant	Washington	DC	\N	\N
Turnagain	Anchorage	AK	\N	1650
South Raleigh	Raleigh	NC	750	995
The Loop	Chicago	IL	1590	2000
Brewerytown	Philadelphia	PA	995	1200
Central City	New Orleans	LA	1100	1400
Bulls Head	New York	NY	\N	2150
SoHo	New York	NY	2495	3299
Fox Creek	Stockton	CA	\N	950
North Ridge-Rosemont	Alexandria	VA	1650	1850
Meiers Corners	New York	NY	\N	\N
Mt. Washington	Cincinnati	OH	535	\N
Cabrillo	Fremont	CA	\N	\N
East Raleigh	Raleigh	NC	695	850
Aurora Highlands	Aurora	CO	725	1400
Eureka Valley - Dolores Heights - Castro	San Francisco	CA	3300	3995
Aurora Highlands	Arlington	VA	1939	2153
Graniteville	New York	NY	\N	1600
Rosebank	New York	NY	\N	1450
North Hyde Park	Tampa	FL	1050	1400
Drake	Des Moines	IA	\N	600
Admiral	Seattle	WA	\N	1195
Carmel Mountain	San Diego	CA	1670	1800
Jamestown	Augusta	GA	\N	895
River Mountain	Henderson	NV	1150	1100
Battery Park	New York	NY	3095	3665
Grandmont-Rosedale	Detroit	MI	\N	800
Waialae-Kahala	Honolulu	HI	5900	6000
Midway District	San Diego	CA	\N	\N
Portland	Louisville	KY	\N	575
Colina del Sol	San Diego	CA	725	950
Villages of Woodland Springs	Fort Worth	TX	\N	1550
Peabody	Cambridge	MA	1850	2200
Clark Fulton	Cleveland	OH	\N	\N
Chinatown	New York	NY	2900	2700
Edison Park	Chicago	IL	1500	1350
Near East	Dallas	TX	1822	1498
St. George	New York	NY	1815	1800
Wicker Park	Chicago	IL	1875	2100
Sunset Arcre, Garden Valley, Morningside	Shreveport	LA	\N	\N
Scott Park	Toledo	OH	\N	699
Radnor-Ft Myer Heights	Arlington	VA	2600	2409
Whitney Ranch	Henderson	NV	\N	1250
Roosevelt Island	New York	NY	3095	2825
Myers Park	Charlotte	NC	1500	1331
College Park	Orlando	FL	1050	995
Western Addition	San Francisco	CA	2285	3750
Crescenta Highlands	Glendale	CA	\N	\N
Speer	Denver	CO	850	1130
Washington Park	Chicago	IL	900	1100
Valencia Park	San Diego	CA	\N	1750
North Broadway	Newark	NJ	\N	1150
Twin Lakes	Las Vegas	NV	650	675
East Village	Long Beach	CA	950	1100
Rose Park	Salt Lake City	UT	\N	1250
Stapleton	New York	NY	\N	2200
Maple Leaf	Seattle	WA	1275	1400
Georgetown	New York	NY	1600	1745
Schiller Park	Buffalo	NY	\N	\N
Flowing Wells	Tucson	AZ	\N	675
Montopolis	Austin	TX	\N	\N
Five Points	El Paso	TX	\N	595
Downtown	Riverside	CA	900	1095
Power Ranch	Gilbert	AZ	\N	1295
Canton	Baltimore	MD	1780	1987
Stonestown	San Francisco	CA	2250	2649
Highland Square	Akron	OH	\N	650
Sellwood-Moreland	Portland	OR	\N	1500
Elmhurst	Providence	RI	950	1500
Sheffield Neighbors	Chicago	IL	1650	1995
Eastmoor	Columbus	OH	\N	675
Brookville	New York	NY	1600	1400
Pine Point	Springfield	MA	\N	1100
North Deering	Portland	ME	\N	\N
Love Field Area	Dallas	TX	899	1035
Olde Torrance	Torrance	CA	\N	1695
Potrero Hill	San Francisco	CA	\N	3950
Forestville	Cincinnati	OH	815	\N
East Hyde Park	Chicago	IL	1150	1245
Mill Creek	Philadelphia	PA	1500	1500
Elmwood	Providence	RI	\N	1025
Brightmoor	Detroit	MI	\N	700
Old Town	Chicago	IL	1760	1900
Upper Baseline	Little Rock	AR	\N	\N
Leimert Park	Los Angeles	CA	1550	1900
Murray Hill	New York	NY	2600	3150
Northwest Crossing	San Antonio	TX	\N	1000
North East	Hartford	CT	650	900
Normal Heights	San Diego	CA	900	1195
Glendale - Heather Downs	Toledo	OH	724	\N
South Collinwood	Cleveland	OH	\N	\N
Crestview	Los Angeles	CA	\N	1550
Franklin Park	Detroit	MI	\N	675
West 7th	Saint Paul	MN	970	1099
Forest Hills	Cleveland	OH	\N	\N
Kashmere Gardens	Houston	TX	\N	775
La Sierra Acres	Riverside	CA	\N	1475
Highland Park	San Antonio	TX	\N	650
Rosemont	Fort Worth	TX	\N	\N
Garrison Park	Austin	TX	950	1045
North Oakland	Pittsburgh	PA	1175	\N
Heron Walk	Nashville	TN	660	\N
Pittman	Henderson	NV	815	875
Ocean Crest	San Diego	CA	\N	2500
Rossville	New York	NY	\N	2650
North Panhandle	San Francisco	CA	2495	3500
Haight-Ashbury	San Francisco	CA	1700	2800
Six Forks	Raleigh	NC	895	1100
East Forest Park	Springfield	MA	\N	\N
Fairview	Hayward	CA	\N	\N
Eagle River Valley	Anchorage	AK	\N	1995
Mission Terrace	San Francisco	CA	\N	\N
Lackland Terrace	San Antonio	TX	\N	\N
Arlington	Riverside	CA	\N	1215
Terrace	San Bernardino	CA	\N	1295
Mount Pleasant	Providence	RI	\N	900
Brookside	Stockton	CA	1245	1500
East Colfax	Denver	CO	845	1020
Chestnut Hill	Philadelphia	PA	1119	1195
Union Miles Park	Cleveland	OH	\N	\N
Hunters Point	New York	NY	2650	2800
University Heights	Newark	NJ	\N	\N
Seventh Ward	New Orleans	LA	\N	850
Asylum Hill	Hartford	CT	729	800
Hegewisch	Chicago	IL	\N	1050
College East	San Diego	CA	1275	3200
Bridle Trails	Bellevue	WA	1365	1650
Baymeadows	Jacksonville	FL	804	979
Sabre Springs	San Diego	CA	2000	1975
Mount Tabor	Portland	OR	\N	\N
Forest	Buffalo	NY	\N	\N
Foxhill	Hampton	VA	1250	1295
Red Hook	New York	NY	1650	3000
Congress Park	Denver	CO	\N	1000
Lower Roseville	Newark	NJ	\N	1100
Rio Bravo	Bakersfield	CA	\N	864
Indian Hills-Stonewall Estates-Monticello	Lexington	KY	\N	\N
Southeast Torrance	Torrance	CA	\N	\N
Paradise Hills	Henderson	NV	\N	1425
Brooklyn	Baltimore	MD	675	900
Turtle Rock	Irvine	CA	2900	2825
University Area	Anchorage	AK	\N	\N
Huguenot	New York	NY	\N	1200
Carrick	Pittsburgh	PA	\N	695
Jenkins, Pinecroft Subdivision	Shreveport	LA	\N	\N
Old Fourth Ward	Atlanta	GA	1035	1313
Mission Valley East	San Diego	CA	1670	1900
Vineyard	Glendale	CA	\N	\N
Kensington	Buffalo	NY	\N	\N
Mission Bay Park	San Diego	CA	1500	1999
Midtown	Palo Alto	CA	\N	3295
Marcy Holmes	Minneapolis	MN	1000	2250
Fernwood	Chicago	IL	\N	1500
Kingman Park	Washington	DC	1450	1995
Midland Beach	New York	NY	\N	1600
Stone Oak	San Antonio	TX	1095	1405
Roscoe Village	Chicago	IL	1395	1750
Jomacha-Lomita	San Diego	CA	\N	\N
Rancho West	San Bernardino	CA	\N	\N
Historic Midtown	Wichita	KS	\N	\N
Kingsgate	Kirkland	WA	999	2195
Great Neck Village	Great Neck	NY	\N	2950
Westside	Santa Barbara	CA	\N	\N
Ballantyne West	Charlotte	NC	1000	1425
Rose Park	Long Beach	CA	975	1200
North End	Boston	MA	2000	2450
Fairlington-Shirlington	Arlington	VA	1900	2150
North Queen Anne	Seattle	WA	1320	1550
Montclaire South	Charlotte	NC	600	900
Oak Creek	Irvine	CA	1950	2265
Park Hill	New York	NY	\N	\N
Burnside	Chicago	IL	\N	925
Jackson Triangle	Hayward	CA	1099	\N
Merle Hay	Des Moines	IA	\N	650
Mandarin	Jacksonville	FL	\N	1500
Clairemont Mesa West	San Diego	CA	\N	\N
West Meadows	Tampa	FL	1050	1300
East Falls	Philadelphia	PA	1250	1295
Pomonok	New York	NY	1700	1880
Old Louisville	Louisville	KY	519	550
Budlong Woods	Chicago	IL	935	1250
Reservorir	Lexington	KY	670	695
Airport	Riverside	CA	\N	1295
Tam O'Shanter	Stockton	CA	\N	1075
Oakley	Cincinnati	OH	1100	1350
Los Angeles Heights - Keystone	San Antonio	TX	\N	799
Portsmouth	Portland	OR	\N	1025
Highlands	Jacksonville	FL	630	890
Highland Hills	Henderson	NV	1100	1250
Richmond Town	New York	NY	\N	1995
South Arroyo	Pasadena	CA	2249	3200
Southwest Ada County Alliance	Boise	ID	\N	\N
Ruby Hill	Denver	CO	\N	\N
College Hill	Providence	RI	1300	1300
Eagle River	Anchorage	AK	\N	1800
East Rock	New Haven	CT	1100	1300
Eastlake Greens	Chula Vista	CA	\N	2150
Frog Hollow	Hartford	CT	950	900
Warm Springs	Fremont	CA	\N	\N
Sunset Hills	Reston	VA	2100	2100
Churchill Area	Eugene	OR	\N	950
Prince's Bay	New York	NY	\N	1000
Beverly	Toledo	OH	\N	\N
Los Altos	Long Beach	CA	\N	\N
Tottenville	New York	NY	\N	1700
Ingleside	San Francisco	CA	\N	\N
Verdugo Viejo	Glendale	CA	1750	1925
West Colfax	Denver	CO	700	\N
Cudell	Cleveland	OH	\N	\N
Wiehle Ave - Reston Pky	Reston	VA	1511	1750
West Kensington	Philadelphia	PA	1400	1650
Near Northeast	Syracuse	NY	\N	\N
Belmont	Dayton	OH	525	\N
Falcon	Colorado Springs	CO	1250	1350
Parker Lane	Austin	TX	745	950
College West	San Diego	CA	1125	1950
Sunnyside	Denver	CO	\N	1200
Florida Center North	Orlando	FL	750	850
Overtown	Miami	FL	1250	1250
East Cambridge	Cambridge	MA	2688	3000
Waterloo	Stockton	CA	\N	750
Cedar-Riverside	Minneapolis	MN	890	\N
American University Park	Washington	DC	2350	1850
Lake Mohawk	Sparta	NJ	2200	2200
Neighbors Southwest	Beaverton	OR	850	1167
Boulevard Heights	Saint Louis	MO	\N	\N
Petosky-Otsego	Detroit	MI	\N	525
Wrightwood Neighbors	Chicago	IL	2050	2395
Yorkmount	Charlotte	NC	670	825
Moanalua	Honolulu	HI	\N	\N
Concordia	Portland	OR	\N	1795
West Bench	Boise	ID	\N	925
Central City	Salt Lake City	UT	1040	1125
Ohio City - West Side	Cleveland	OH	\N	\N
University	Denver	CO	\N	1450
Shearer Hills - Ridgeview	San Antonio	TX	\N	1195
Lyell-Otis	Rochester	NY	\N	750
Deep Creek South	Chesapeake	VA	\N	1950
Lindenwood Park	Saint Louis	MO	\N	700
Southwood Riviera	Torrance	CA	\N	\N
North Hills	El Paso	TX	\N	1300
Cherry Avenue	Tucson	AZ	\N	800
Murray Hill	Jacksonville	FL	750	750
Castle	San Diego	CA	\N	1100
Sans Pareil	Jacksonville	FL	900	\N
Victoria	Riverside	CA	\N	1675
Avenues West	Milwaukee	WI	853	\N
Mustang-Padre Island	Corpus Christi	TX	1250	1600
Rose City Park	Portland	OR	\N	1895
Woodhaven	Fort Worth	TX	\N	591
Behind the Rocks	Hartford	CT	750	\N
Barton-McFarland	Detroit	MI	\N	750
Near South	Lincoln	NE	\N	\N
North Juanita	Kirkland	WA	1200	1320
Vista	Boise	ID	650	795
East Bench	Salt Lake City	UT	\N	\N
Wade	Raleigh	NC	995	1050
Martin Luther King Dr. Area	Shreveport	LA	\N	489
Torrey Pines	San Diego	CA	\N	\N
Shaw	Washington	DC	1950	2422
Irvington	Fremont	CA	1440	1950
Belltown	Seattle	WA	1600	1700
Beacon Hill	Boston	MA	1850	2550
Queensborough	Shreveport	LA	\N	\N
Charles Village	Baltimore	MD	850	890
Oak Park - Northwood	San Antonio	TX	\N	1400
South East	Pasadena	CA	1700	1500
Mill Park	Portland	OR	\N	\N
Park Place	Houston	TX	\N	\N
Handley	Fort Worth	TX	\N	999
Midtown West	Stockton	CA	800	525
North River	Toledo	OH	\N	\N
North Park Hill	Denver	CO	\N	1300
Superstition Springs	Mesa	AZ	845	924
West Meadowbrook	Fort Worth	TX	\N	\N
Chinatown	Boston	MA	2495	3000
Scenic Foothills	Anchorage	AK	\N	1800
North End	Boise	ID	595	600
Washington School	Long Beach	CA	\N	1038
Southwest Waterfront	Washington	DC	1750	2100
Beverlywood	Los Angeles	CA	3650	1680
Oakland	Pittsburgh	PA	1350	1000
St. Johns	Austin	TX	779	840
Athmar Park	Denver	CO	\N	\N
Glenwood	Glendale	CA	\N	\N
Steele Creek	Charlotte	NC	1150	1200
Evanston	Cincinnati	OH	\N	825
Toluca Lake	Los Angeles	CA	2850	2025
Van Buskirk	Stockton	CA	\N	1050
Fair Oaks	Stockton	CA	\N	\N
Water Catchment Area	West Palm Beach	FL	1100	1450
Downtown	Cleveland	OH	1080	1900
Holly	Everett	WA	945	1150
Douglas Park	Arlington	VA	1925	2200
Woodstock	Portland	OR	\N	1195
Talmadge	San Diego	CA	995	1095
Spanos Park East	Stockton	CA	\N	1475
Northside	Riverside	CA	\N	1500
University of Texas	Austin	TX	900	\N
Airport, Pines Road	Shreveport	LA	620	\N
Indian Orchard	Springfield	MA	\N	900
Phinney Ridge	Seattle	WA	1500	1250
Eastchester	New York	NY	\N	1370
Cleveland Park	Washington	DC	1900	1575
Greenridge	New York	NY	\N	\N
Villa Park	Denver	CO	\N	900
Hyde Park	Jacksonville	FL	895	895
Lincoln Park	San Diego	CA	\N	\N
Mission Grove	Riverside	CA	1265	1550
Greenland	Jacksonville	FL	1350	1550
South Knoxville	Knoxville	TN	620	645
Edison	Kalamazoo	MI	\N	695
South Central Improvemen	Wichita	KS	\N	550
Isle of Normandy	Miami Beach	FL	\N	1800
Heritage	Fort Worth	TX	\N	2100
Greenhaven	Sacramento	CA	885	1040
Wilkes	Portland	OR	\N	\N
Anderson	Stockton	CA	800	750
Bear Valley	Denver	CO	\N	\N
Lincoln Village West	Stockton	CA	950	\N
Southside Estates	Jacksonville	FL	795	925
Russell	Louisville	KY	\N	650
West Highland	Denver	CO	\N	1500
Redwood Heights	Oakland	CA	1250	\N
Powderhorn Park	Minneapolis	MN	895	\N
Emerson-Garfield	Spokane	WA	\N	650
Little Italy	New York	NY	3000	3450
Southland-Deerfield-Open Gates	Lexington	KY	\N	950
Clifton	Cincinnati	OH	\N	\N
Temple Crest	Tampa	FL	705	950
Madisonville	Cincinnati	OH	850	895
Beechwood	Rochester	NY	\N	\N
North Arroyo	Pasadena	CA	\N	\N
Oak Forest	Little Rock	AR	\N	650
Windsor Spring	Augusta	GA	\N	750
Golden Hill	San Diego	CA	1095	1550
Mount Washington	Pittsburgh	PA	900	1100
Harford-Echodale - Perring Parkway	Baltimore	MD	\N	850
Midtown	Houston	TX	1410	1769
Trumbull Village	Albuquerque	NM	\N	450
Westwood	Kalamazoo	MI	641	860
Shipley Terrace	Washington	DC	\N	\N
Mesa Hills	El Paso	TX	\N	\N
Georgian Acres	Austin	TX	715	810
West Meade	Nashville	TN	950	1150
Central Davis	Davis	CA	\N	2195
Mt. Airy	Cincinnati	OH	\N	\N
Village East	Aurora	CO	769	\N
Benton Park	Bakersfield	CA	\N	\N
South Linden	Columbus	OH	575	650
Highland	Denver	CO	1375	1730
Woodland Hills	Cleveland	OH	\N	\N
Coulwood West	Charlotte	NC	995	1050
Falls of Neuse	Raleigh	NC	1195	1095
West Cambridge	Cambridge	MA	2300	2500
Willowbrook	Houston	TX	695	1175
Sierra del Oro	Corona	CA	\N	2199
Rossmoyne	Glendale	CA	\N	\N
Rosemoor	Chicago	IL	\N	900
South Park Hill	Denver	CO	\N	1069
Green Lake	Seattle	WA	\N	1775
Downtown East	Las Vegas	NV	\N	550
Willard Hay	Minneapolis	MN	995	\N
Mountain View	Anchorage	AK	\N	\N
South Hills	Fort Worth	TX	\N	\N
Brightwood	Washington	DC	\N	1439
Pine Hills	Atlanta	GA	1250	1400
Riverside	Jacksonville	FL	950	750
Liberty Wells	Salt Lake City	UT	\N	825
South Beaverton	Beaverton	OR	\N	\N
Egger Highlands	San Diego	CA	\N	\N
Belmont Shore	Long Beach	CA	1700	1795
Skyline	San Diego	CA	\N	1800
Highland Park	Des Moines	IA	\N	\N
Yerdemont	San Bernardino	CA	1095	1475
Northeast Macfarlane	Tampa	FL	\N	900
Buckman	Portland	OR	1095	1295
Englewood	Jacksonville	FL	895	950
Haller Lake	Seattle	WA	\N	1500
Northwest Los Angeles Heights	San Antonio	TX	\N	\N
Woodbury	Irvine	CA	1885	2050
Fort Logan	Denver	CO	\N	\N
Riverbend	Columbus	OH	\N	\N
Bloomfield	Pittsburgh	PA	1095	1200
Central Hilltop	Columbus	OH	635	600
Powelton	Philadelphia	PA	790	1249
Harvey Park South	Denver	CO	\N	\N
Richmond Hill	Augusta	GA	\N	575
Langwood	Houston	TX	580	\N
Delthome	Torrance	CA	\N	1325
Broadview	Seattle	WA	\N	1750
Providence Plantation	Charlotte	NC	\N	\N
Campbell Park	Anchorage	AK	\N	\N
Plaza Terrace	Tampa	FL	670	839
Independence Village	Columbus	OH	1000	1050
Brooklyn Centre	Cleveland	OH	\N	\N
Cow Hollow	San Francisco	CA	\N	3600
University of Ohio Akron	Akron	OH	690	500
Southwest	San Antonio	TX	\N	\N
Park West	San Diego	CA	1695	1550
Elvira	Tucson	AZ	\N	582
Engelwood Park	Orlando	FL	\N	875
Ballantyne East	Charlotte	NC	935	1249
Manor Park	Washington	DC	\N	1395
Laurelglen	Bakersfield	CA	\N	1125
Central	Minneapolis	MN	\N	\N
Mid Central	Pasadena	CA	1800	1925
University Park	Irvine	CA	2600	2275
Corridor	San Diego	CA	775	1025
Bitter Lake	Seattle	WA	1200	1295
Near Northeast	Washington	DC	1995	2300
Oak Hill	Jacksonville	FL	875	925
Grantville	San Diego	CA	1398	1920
Cliff-Cannon	Spokane	WA	\N	550
Noble Square	Chicago	IL	1795	1700
Franklinton	Columbus	OH	\N	\N
Hilltop	Denver	CO	\N	1975
Midtown	Little Rock	AR	774	895
Rainbow Hills	San Antonio	TX	682	\N
Riverside	Columbus	OH	765	810
Clintonville	Columbus	OH	\N	\N
Westmont	Everett	WA	\N	995
Westpointe	Salt Lake City	UT	\N	\N
Charlotte	Rochester	NY	\N	\N
Berkeley	Denver	CO	\N	1500
Sandtown-Winchester	Baltimore	MD	\N	950
Pacific Edison	Glendale	CA	\N	2536
Marshbrooke	Charlotte	NC	750	975
Otay Ranch Village 1	Chula Vista	CA	1685	2189
Bel Air	Los Angeles	CA	6350	3535
Lowry Field	Denver	CO	1000	1335
Rockaway Beach	New York	NY	\N	1550
South Middle River	Fort Lauderdale	FL	1350	1235
North Buckhead	Atlanta	GA	1710	1705
Castleton Corners	New York	NY	\N	1350
Southwest Richardson	Richardson	TX	\N	\N
Barton Hills	Austin	TX	1070	1460
Morningside - Lenox Park	Atlanta	GA	2000	\N
Old Seward-Oceanview	Anchorage	AK	\N	\N
Mineral Springs-Rumble Road	Charlotte	NC	797	995
Toddville Road	Charlotte	NC	750	925
Glen	Baltimore	MD	\N	\N
Thoroughgood	Virginia Beach	VA	\N	1500
Vose	Beaverton	OR	\N	\N
Hickory Ridge	Charlotte	NC	775	895
Beechmont	Louisville	KY	\N	\N
Piper Glen Estates	Charlotte	NC	1250	1100
Roosevelt	Bellingham	WA	750	710
Downtown	Saint Paul	MN	975	1211
Airport North	Orlando	FL	825	999
Creston-Kenilworth	Portland	OR	\N	945
South-West Coconut Grove	Miami	FL	2400	3000
Quintana Community	San Antonio	TX	\N	\N
Edgerton	Rochester	NY	\N	550
East Village	San Diego	CA	2045	2350
Windsor Terrace	New York	NY	1595	2200
Natomas Park	Sacramento	CA	\N	1645
Capitol Hill	Salt Lake City	UT	\N	850
West Woodlawn	Chicago	IL	950	1100
Southwest	Columbus	OH	\N	\N
Jewell Heights - Hoffman Heights	Aurora	CO	895	1295
DMV	San Bernardino	CA	\N	750
Springfield Gardens	New York	NY	1650	1500
Redwood Village	San Diego	CA	\N	1400
University District	Cleveland	OH	\N	\N
Newport Hills	Bellevue	WA	\N	\N
Central Oak Park	Saint Petersburg	FL	811	800
Brentwood	Austin	TX	1195	1339
Eastland	Columbus	OH	\N	\N
Marble Hill	New York	NY	1550	1250
Craven	Jacksonville	FL	700	1197
Olympic Hills	Seattle	WA	\N	1395
Carriage Place	Aurora	CO	\N	\N
Port Gardner	Everett	WA	995	\N
South Juanita	Kirkland	WA	1299	1395
Northgate	Columbus	OH	607	\N
West End	Hartford	CT	800	795
Cheesman Park	Denver	CO	1300	945
Grymes Hill	New York	NY	\N	3100
Avondale	Cincinnati	OH	\N	630
Behrman	New Orleans	LA	\N	\N
Arrochar	New York	NY	\N	1325
North Hampton	Saint Louis	MO	550	550
Oak Park	Santa Barbara	CA	\N	1225
Greater Harmony Hills	San Antonio	TX	659	875
Clarendon-Courthouse	Arlington	VA	2315	2635
Northeast Park Hill	Denver	CO	\N	\N
Allandale	Austin	TX	1300	1430
Chicot West I-30 So.	Little Rock	AR	\N	\N
Heninger Park	Santa Ana	CA	\N	\N
Bond Hill	Cincinnati	OH	\N	\N
Loring Park	Minneapolis	MN	995	970
Sweetwater	Columbus	OH	\N	1150
Washington Park	Providence	RI	\N	1575
Southside	Augusta	GA	\N	\N
Harris-Houston	Charlotte	NC	765	600
River North	Chicago	IL	2095	2198
Wedgwood	Seattle	WA	1140	\N
Country Club Hills, Lakeshore Shopping	Shreveport	LA	\N	\N
Loyal Heights	Seattle	WA	\N	1795
Clason Point	New York	NY	\N	1600
Five Points	Raleigh	NC	1195	1150
Eastside	Santa Barbara	CA	\N	\N
Glen Park	San Francisco	CA	\N	3975
Walnut Heights	Columbus	OH	\N	900
Midtown	Detroit	MI	1000	\N
Walnut Village	Irvine	CA	\N	2680
Otay Ranch Village 5	Chula Vista	CA	\N	2200
Adams Point	Oakland	CA	1195	1550
Palmer Square	Chicago	IL	1395	1600
Madison South	Portland	OR	799	\N
Santa Clara	Hayward	CA	\N	1801
Downtown	New York	NY	2500	2971
Everett Mall South	Everett	WA	899	\N
East Springfield	Springfield	MA	\N	1100
Hattontown	Reston	VA	\N	1800
Kenton	Portland	OR	\N	1300
South Beach	New York	NY	\N	1250
Minor	Seattle	WA	1447	1490
Expo Park	Aurora	CO	\N	900
South Lamar	Austin	TX	932	1310
Linden Hills	Minneapolis	MN	950	1685
Bemiss	Spokane	WA	\N	\N
Lakewood Village	Long Beach	CA	\N	\N
MLK 183	Austin	TX	950	\N
Niles	Fremont	CA	\N	\N
Riggs Park	Washington	DC	\N	1801
Westville	New Haven	CT	1070	1200
Glover Park	Washington	DC	1918	1861
Telegraph Hill	San Francisco	CA	3000	3975
Mission-Garin	Hayward	CA	1150	\N
Gleason Park	Stockton	CA	\N	675
Old Town Triangle	Chicago	IL	1450	2050
Pleasant Ridge	Cincinnati	OH	650	550
Cherry Creek	Columbus	OH	\N	\N
Arrowhead	San Bernardino	CA	\N	1200
Edgewater	Cleveland	OH	595	650
Quail Lakes - Venetian Bridges	Stockton	CA	975	900
Moran Prairie	Spokane	WA	\N	\N
Forest Hills	Tampa	FL	914	1050
Upper Hill	Springfield	MA	\N	950
Glenwood	Raleigh	NC	\N	\N
Jackson Park	Milwaukee	WI	\N	\N
Deerwood	Jacksonville	FL	1050	1285
Jordan	Minneapolis	MN	945	1000
Walnut Valley	Little Rock	AR	745	850
St. Louis Hills	Saint Louis	MO	\N	650
Chinatown	Los Angeles	CA	\N	2145
Family Acres	Lincoln	NE	\N	\N
Northside	Cincinnati	OH	\N	595
Rosemont	Orlando	FL	675	795
Twin Rivers	East Windsor	NJ	\N	\N
South Central	Raleigh	NC	\N	700
Riverside	Wichita	KS	550	\N
West Central	Spokane	WA	\N	575
Carondelet	Saint Louis	MO	525	575
Woodland Acres	Jacksonville	FL	\N	790
Sunbow II	Chula Vista	CA	\N	\N
Arlington Hills	Jacksonville	FL	900	995
Clinton	Oakland	CA	\N	\N
Multnomah	Portland	OR	999	950
Lauderdale Manors	Fort Lauderdale	FL	1500	1300
Verdugo Woodlands	Glendale	CA	\N	\N
Lovejoy	Buffalo	NY	\N	\N
Parkwoods	Stockton	CA	\N	850
Somerset	Columbus	OH	\N	\N
West Augusta	Augusta	GA	649	\N
University Park	Denver	CO	\N	905
Land Park	Sacramento	CA	\N	1100
University District	Missoula	MT	\N	895
Reservoir	Little Rock	AR	585	725
Mayfair	Chicago	IL	\N	950
West Sugar Creek-W T Harris Bl	Charlotte	NC	850	1000
Longwood Manor	Chicago	IL	\N	\N
East Ballard	Seattle	WA	\N	2200
Ballard	Seattle	WA	\N	1790
Spice Tract	Bakersfield	CA	\N	\N
Loretto	Jacksonville	FL	850	1175
North Mayfair	Chicago	IL	\N	\N
La Mesa	Albuquerque	NM	\N	500
Kingfield	Minneapolis	MN	\N	1150
Mission-Foothill	Hayward	CA	1200	1511
Cedar Hills	Jacksonville	FL	850	895
Coldstream Homestead Montebello	Baltimore	MD	1000	1000
Milwood	Kalamazoo	MI	\N	\N
Morena	San Diego	CA	1799	2150
Mount Scott	Portland	OR	\N	\N
South San Pedro	Albuquerque	NM	\N	650
Prospect Park	Minneapolis	MN	1180	1500
Crystal Springs	Jacksonville	FL	\N	1200
Lyndale	Minneapolis	MN	\N	\N
Cherry Hill	Baltimore	MD	\N	899
Stockyards	Cleveland	OH	\N	\N
Collister	Boise	ID	\N	675
Mount Pleasant	Newark	NJ	\N	\N
Princeton Heights	Saint Louis	MO	\N	725
Old Town	New York	NY	\N	1600
Foster-Powell	Portland	OR	\N	\N
Thunderbird Hills	San Antonio	TX	620	1275
Wilburton	Bellevue	WA	\N	2100
Columbia City	Seattle	WA	\N	1288
Cheswolde	Baltimore	MD	860	949
Glencliff	Nashville	TN	790	\N
Brookvale	Fremont	CA	1475	\N
Starmount Forest	Charlotte	NC	645	700
Catholic University	Washington	DC	\N	\N
Wellswood	Tampa	FL	609	\N
The Islands	Gilbert	AZ	1350	1300
Hartford	Providence	RI	\N	\N
Broadway-Fillmore	Buffalo	NY	\N	\N
East	Columbus	OH	\N	\N
St. Anthony	Saint Paul	MN	1132	1025
Downtown	Austin	TX	1408	2195
Schorsch Village	Chicago	IL	\N	\N
Franklin to the Fort	Missoula	MT	\N	615
Cleveland Heights	Oakland	CA	\N	1800
Virginia Highland	Atlanta	GA	1210	1100
Silver Lake	Everett	WA	925	1155
Country Club	New York	NY	\N	1700
Greenfield	Pittsburgh	PA	\N	\N
Federal Hill	Providence	RI	999	1395
Sloan Lake	Denver	CO	\N	\N
Brick Church Bellshire	Nashville	TN	\N	\N
Lake	San Francisco	CA	\N	4300
West Hill	Albany	NY	\N	840
Woodlawn	New York	NY	\N	1400
Robla	Sacramento	CA	\N	1195
Brookland	Washington	DC	\N	1650
Fair Haven Heights	New Haven	CT	\N	1400
Thompson Community	San Antonio	TX	\N	\N
Old Town	Alexandria	VA	1295	2100
East Ukrainian Village	Chicago	IL	1450	2275
South Hampton	Saint Louis	MO	\N	750
Sexton Mountain	Beaverton	OR	\N	\N
Dayton Triangle	Aurora	CO	\N	1100
Upper Albany	Hartford	CT	\N	\N
Lone Mountain	San Francisco	CA	\N	\N
Fairview	Anchorage	AK	\N	\N
Delaware Avenue	Albany	NY	\N	945
Alki	Seattle	WA	\N	1395
Grant City	New York	NY	\N	1300
Hillyard	Spokane	WA	\N	785
South City Community	Wichita	KS	\N	650
Brighton Heights	Pittsburgh	PA	\N	\N
Brighton	Seattle	WA	\N	\N
Springdale	Stamford	CT	1500	1700
Cobble Hill	New York	NY	2400	2400
Blacow	Fremont	CA	\N	\N
SBHS	San Bernardino	CA	\N	725
Tri-Village	Columbus	OH	689	780
St. Claire-Superior	Cleveland	OH	\N	\N
Allendale, Lakeside	Shreveport	LA	\N	\N
Historic Old Northeast	Saint Petersburg	FL	750	795
Sunnyside	Portland	OR	1049	1295
Shannon Park	Charlotte	NC	690	850
Acredale	Virginia Beach	VA	\N	1350
Southgate	Bakersfield	CA	\N	\N
Holiday Hill	Jacksonville	FL	900	995
Grasmere - Concord	New York	NY	\N	1350
Central	San Mateo	CA	\N	\N
Downtown	Seattle	WA	1599	2100
Somerset	Glendale	CA	\N	\N
Friendly Area	Eugene	OR	\N	875
Van Steuban	Detroit	MI	\N	650
Western Hills and Yarborough Subdivision	Shreveport	LA	\N	\N
Campus Park	Bakersfield	CA	\N	\N
Grandale	Detroit	MI	\N	650
Hillcrest	Jacksonville	FL	650	845
Mid-Westside	Jacksonville	FL	\N	650
Grant Park	Atlanta	GA	1163	1350
College-Glen	Sacramento	CA	\N	1450
Corbett-Terwilliger-Lair Hill	Portland	OR	1450	1525
Delta	Everett	WA	\N	\N
Old Seminole Heights	Tampa	FL	\N	990
Olneyville	Providence	RI	800	800
Las Sendas	Mesa	AZ	1745	1900
South Manchaca	Austin	TX	950	1010
Margate Park	Chicago	IL	995	1100
East Bakersfield	Bakersfield	CA	\N	595
Julington Creek	Jacksonville	FL	\N	1450
Hunters Green	Tampa	FL	999	1700
Hillsdale	Portland	OR	750	1195
Windsor Hills	Austin	TX	930	\N
Black Mountain	Henderson	NV	950	995
Dwight	New Haven	CT	\N	1195
Mission San Jose	Fremont	CA	\N	\N
Sauganash	Chicago	IL	\N	1700
Borah	Boise	ID	\N	\N
Kenwood	Chicago	IL	930	1250
Blackstone	Providence	RI	1000	1200
Metro Center	Springfield	MA	\N	\N
Five Mile Creek	Dallas	TX	\N	\N
North Tampa	Tampa	FL	\N	800
Mill Basin	New York	NY	\N	1700
Plaza-Eastway	Charlotte	NC	\N	850
New Tampa	Tampa	FL	1295	1350
Seward	Minneapolis	MN	\N	\N
Canyon Creek	Richardson	TX	\N	1750
Kilbourn Park	Chicago	IL	720	850
Mission Viejo	Aurora	CO	\N	\N
Crescent Hill	Louisville	KY	\N	\N
Fitzgerald	Detroit	MI	\N	650
East Queen Anne	Seattle	WA	1650	1600
Dunning	Chicago	IL	\N	1500
Taylor Berry	Louisville	KY	\N	625
Northeast Bakersfield	Bakersfield	CA	\N	750
Washington Park	Denver	CO	\N	2000
Pelican Bay	Naples	FL	3000	5500
Buena Vista	Washington	DC	\N	\N
Newhallville	New Haven	CT	995	1000
Annadale	New York	NY	\N	1200
Boynton	Detroit	MI	\N	\N
Sunbeam	Jacksonville	FL	899	1120
Piedmont	Portland	OR	\N	\N
North College Park	Seattle	WA	915	1495
Havenscourt	Oakland	CA	\N	1100
Wheeless Road	Augusta	GA	\N	\N
Old North Columbus	Columbus	OH	\N	899
Tampa Heights	Tampa	FL	\N	900
North Sharon Amity	Charlotte	NC	695	795
Comstock	Spokane	WA	\N	\N
High Point	Seattle	WA	\N	\N
Bay Terrace	New York	NY	\N	\N
North Avondale	Cincinnati	OH	\N	825
North Indian Trail	Spokane	WA	\N	\N
Hallmark-Camelot	Fort Worth	TX	\N	\N
Meadow Wood	Aurora	CO	\N	\N
Hosford-Abernethy	Portland	OR	\N	1200
Hale	Denver	CO	\N	900
Elliot Park	Minneapolis	MN	900	1450
South Ironbound	Newark	NJ	\N	\N
Summit Hill	Saint Paul	MN	\N	995
Duncan Park	Lexington	KY	\N	\N
Coronado	El Paso	TX	\N	\N
Dietz	Tucson	AZ	\N	1050
North Burnett	Austin	TX	877	\N
Stonewood	Stockton	CA	\N	950
Back Creek Church Road	Charlotte	NC	1200	1200
Bayshore Beautiful	Tampa	FL	1325	1200
Leonidas	New Orleans	LA	\N	900
Kentfield	Stockton	CA	\N	950
Aurora Knolls - Hutchinson Heights	Aurora	CO	\N	\N
Columbia Heights West	Arlington	VA	2010	1275
Far West-Side	Syracuse	NY	\N	\N
St. Claude	New Orleans	LA	\N	\N
Black Mountain Ranch	San Diego	CA	\N	4300
Pinehurst	Everett	WA	\N	950
Sable Altura Chambers	Aurora	CO	\N	\N
Southgate	Hayward	CA	\N	\N
Rainier Beach	Seattle	WA	\N	1550
Tremont	Cleveland	OH	\N	\N
West End	Saint Louis	MO	\N	675
Teralta East	San Diego	CA	\N	875
Ponce de Leon	Stockton	CA	950	750
Howe	Minneapolis	MN	\N	950
Annex	New Haven	CT	\N	850
Del Cerro	San Diego	CA	\N	\N
Amphi	Tucson	AZ	\N	675
Victoria Park	Fort Lauderdale	FL	1895	1650
Mount Vernon Square	Washington	DC	2300	2600
Shaw	Saint Louis	MO	750	775
Center Pointe	Aurora	CO	\N	\N
Airport Heights	Anchorage	AK	\N	\N
Over-The-Rhine	Cincinnati	OH	\N	750
Park Avenue	Rochester	NY	\N	900
Dilworth	Charlotte	NC	1099	1309
Necko	Columbus	OH	\N	545
University Square	Tampa	FL	\N	975
California Heights	Long Beach	CA	\N	1350
Park Stockdale	Bakersfield	CA	\N	1100
Highland	Beaverton	OR	\N	\N
Longwood-Winton Grove	Hayward	CA	\N	\N
Washington Heights	Milwaukee	WI	\N	\N
Riverpark	South Bend	IN	\N	650
Norwood Park West	Chicago	IL	\N	\N
East Avenue	Rochester	NY	885	900
St. Roch	New Orleans	LA	\N	\N
South Dennis	Dennis	MA	\N	\N
Bushrod	Oakland	CA	\N	\N
Eastland-Wilora Lake	Charlotte	NC	700	\N
South Trenton	Trenton	NJ	\N	\N
Idlewild South	Charlotte	NC	750	950
West End	Cincinnati	OH	\N	700
North City	San Diego	CA	\N	4800
Baldwin Park	Orlando	FL	1575	1999
Spanos Park West	Stockton	CA	\N	\N
Ortega Hills	Jacksonville	FL	775	950
Southside Flats	Pittsburgh	PA	1500	1300
Downtown	New Haven	CT	1330	1475
Carmel	Charlotte	NC	\N	\N
Secret Cove	Jacksonville	FL	1050	1150
Oak Forest	Charlotte	NC	550	550
Aurora Hills	Aurora	CO	\N	\N
Glenbrook	Columbus	OH	\N	\N
Wood Streets	Riverside	CA	\N	850
Piedmont Avenue	Oakland	CA	\N	\N
Highland Park	Seattle	WA	\N	\N
Onyx	Toledo	OH	\N	\N
Melrose Park	Fort Lauderdale	FL	1600	1649
Jefferson Chalmers	Detroit	MI	\N	\N
Glade Dr - Reston Pky	Reston	VA	1725	1850
Girvin	Jacksonville	FL	1050	1275
Sheridan Park	Chicago	IL	850	1100
Bryant	Buffalo	NY	625	825
South River City	Austin	TX	1200	1500
Midtown - Winn Park Capital Avenue	Sacramento	CA	\N	895
Walnut Hills	Cincinnati	OH	\N	750
Sharon Heights	Columbus	OH	\N	\N
Denny Whitford - Raleigh West	Beaverton	OR	\N	\N
Bellmont Hillsboro	Nashville	TN	\N	2000
Chesapeake Beach	Virginia Beach	VA	1350	1350
Rancho Del Rey I	Chula Vista	CA	\N	\N
Coomer Creek	Garland	TX	\N	\N
Vista East	Orlando	FL	885	1295
Northside	Fort Wayne	IN	\N	500
Parkmont	Fremont	CA	\N	\N
Winstead Park	Boise	ID	605	\N
Jefferson Westside	Eugene	OR	695	655
Inglewood (Riverwood)	Nashville	TN	\N	1100
Charles	Providence	RI	750	795
View Ridge-Madison	Everett	WA	\N	\N
Ventura Village	Minneapolis	MN	\N	\N
Midtown	Tucson	AZ	650	635
Standish	Minneapolis	MN	\N	1000
North Lamar	Austin	TX	655	\N
Normandy Estate	Jacksonville	FL	\N	\N
Randle Highlands	Washington	DC	\N	\N
South Side	West Palm Beach	FL	1800	1750
Sunset Hill	Seattle	WA	850	2400
Howard Park	Baltimore	MD	\N	\N
Kirkwood	Atlanta	GA	1350	1250
Hackensack Riverfront	Jersey City	NJ	\N	\N
Richmond Factory	Augusta	GA	\N	\N
West Beaverton	Beaverton	OR	\N	\N
Hidden Cove - Indian Creek-Southwest	San Antonio	TX	\N	\N
McMurray - Huntingdon	Nashville	TN	\N	960
Home Park	Atlanta	GA	1110	\N
Seven Hills	Aurora	CO	\N	\N
Rolando	San Diego	CA	1115	1150
West Mesa	Albuquerque	NM	\N	\N
Townsite	Henderson	NV	925	800
Gardenside-Colony	Lexington	KY	\N	675
Clay-Arsenal	Hartford	CT	\N	800
Del Norte	Albuquerque	NM	730	685
South Sundale	Fremont	CA	\N	1712
Arbor Lodge	Portland	OR	\N	1595
Matthews Beach	Seattle	WA	\N	\N
Fairmount Village	San Diego	CA	\N	\N
University Park	San Antonio	TX	\N	\N
Seminole Heights	Tampa	FL	\N	1200
Lakeview	New Orleans	LA	\N	\N
Lower Garden District	New Orleans	LA	1350	2900
University Hill	Boulder	CO	2475	2490
Hollywood Park	Chicago	IL	\N	\N
Sunrise Neighborhood Coalition	San Antonio	TX	\N	895
South Area	Wichita	KS	\N	\N
Montrose Verdugo City	Glendale	CA	\N	\N
Farm Pond	Charlotte	NC	\N	850
Bluemont	Arlington	VA	1756	1825
Highland Park	Pittsburgh	PA	\N	1100
Gatewood	Seattle	WA	\N	\N
Goose Hollow	Portland	OR	1325	1595
Wellington-Harrington	Cambridge	MA	2100	2400
Elyria Swansea	Denver	CO	\N	\N
Dixwell	New Haven	CT	\N	\N
Upper Dimond	Oakland	CA	\N	1200
Washington Park West	Denver	CO	\N	1495
Brentwood	Jacksonville	FL	695	725
Laredo Highline	Aurora	CO	\N	\N
Saint Joseph	Milwaukee	WI	\N	\N
College Downs	Charlotte	NC	709	800
St. Elizabeth	Oakland	CA	\N	\N
Uptown	Milwaukee	WI	\N	\N
North Park	Chicago	IL	875	1000
Downtown	Columbus	OH	1000	845
Westchester-Green Countrie	Columbus	OH	659	1200
East Chatham	Chicago	IL	675	700
North Beach	San Francisco	CA	\N	4750
Chief Garry Park	Spokane	WA	\N	595
Adams Hill	Glendale	CA	\N	\N
Overlook	Portland	OR	\N	\N
Veterans Park	Boise	ID	650	675
North Lake	Charlotte	NC	1000	1085
Roseway	Portland	OR	\N	1195
Southwood	Torrance	CA	\N	2695
Roselawn	Cincinnati	OH	\N	600
Turtle Creek	Jacksonville	FL	799	1100
Alanton	Virginia Beach	VA	1099	1150
The Museum District	Richmond	VA	805	900
Linwood	Columbus	OH	\N	\N
South Tabor	Portland	OR	\N	\N
Argay	Portland	OR	\N	\N
King	Portland	OR	\N	895
North Rose Hill	Kirkland	WA	\N	1325
Springfield	Jacksonville	FL	750	775
Imperial Point	Fort Lauderdale	FL	1695	1295
Fircrest	Vancouver	WA	\N	\N
Central Park Heights	Baltimore	MD	\N	995
Val Vista Lakes	Gilbert	AZ	1200	1700
Quinnipiac	New Haven	CT	\N	\N
Lowry Hill East	Minneapolis	MN	1230	1500
Glenham-Belford	Baltimore	MD	\N	1050
Merriman Valley	Akron	OH	629	\N
The Port - Area 4	Cambridge	MA	2100	2500
Corbett	Tucson	AZ	\N	750
Ocotillo	Chandler	AZ	1695	1900
JeffVanderLou	Saint Louis	MO	850	\N
Waltherson	Baltimore	MD	\N	\N
Del Mar Heights	San Diego	CA	3200	3200
Saddle Rock Golf Club	Aurora	CO	1099	\N
New Brighton	New York	NY	\N	1650
Cardinal Hill-Pine Meadow	Lexington	KY	\N	\N
Linkhorn Park	Virginia Beach	VA	1065	1295
Jungle Terrace	Saint Petersburg	FL	\N	\N
Lincoln Park	Denver	CO	\N	\N
Alta Mesa	Mesa	AZ	750	1100
Ingleside Heights	San Francisco	CA	\N	\N
Irvington	Portland	OR	895	1495
Great Neck Plaza	Great Neck	NY	1732	2362
Weberstown	Stockton	CA	\N	\N
Forest Hills	Washington	DC	2195	1870
Barnum	Denver	CO	\N	\N
Reservoir Hill	Baltimore	MD	950	1095
University Park	Portland	OR	\N	\N
West University	Eugene	OR	\N	850
Kendall - Whittier	Tulsa	OK	\N	\N
Depot Bench	Boise	ID	750	\N
Dunlap	Seattle	WA	\N	\N
Bon Air	Louisville	KY	\N	\N
Congress Heights	Washington	DC	1025	1225
Kensington	San Diego	CA	\N	1095
University Town Center	Irvine	CA	\N	2100
Central Downtown	Lexington	KY	\N	775
South Shoreview	San Mateo	CA	\N	\N
San Jose	Jacksonville	FL	667	559
Chickasaw	Louisville	KY	\N	700
Hampden	Baltimore	MD	\N	\N
Sunflower	Wichita	KS	\N	675
Mount Hope	Providence	RI	1000	1150
Fairpark	Salt Lake City	UT	\N	\N
Wessex Square	Charlotte	NC	855	\N
West Henderson	Henderson	NV	\N	1500
Penn Wynne	Wynnewood	PA	\N	\N
East Lake I	Chula Vista	CA	\N	1800
Silver Creek	Bakersfield	CA	\N	1450
Elmwood Park	Detroit	MI	815	800
Tompkinsville	New York	NY	\N	1800
Core-Columbia	San Diego	CA	2045	2150
La Jolla Village	San Diego	CA	2000	1925
Greenway	Beaverton	OR	\N	\N
Hillcrest	Little Rock	AR	800	775
Ukrainian Village	Chicago	IL	1350	1550
Fishers Landing East	Vancouver	WA	\N	\N
Meadowlawn	Saint Petersburg	FL	\N	985
Tower Grove East	Saint Louis	MO	650	750
South Patrick Shores	Satellite Beach	FL	975	1050
Columbia Heghts	Arlington	VA	1480	1600
New Aurora-English Turn	New Orleans	LA	\N	\N
Highland	Rochester	NY	\N	\N
Naples Park	Naples	FL	1850	\N
Parkrose	Portland	OR	\N	\N
Cherry-Guardino	Fremont	CA	1675	2235
Uptown	New Orleans	LA	\N	1775
Indianola Hills	Des Moines	IA	\N	\N
Taylor Run	Alexandria	VA	1411	1600
Beverly Woods	Charlotte	NC	1100	\N
Gateway West	Sacramento	CA	\N	1295
Academy Acres North	Albuquerque	NM	\N	\N
Junction	Seattle	WA	1200	1435
Glynlea - Grove Park	Jacksonville	FL	670	\N
Lynnhaven Shores	Virginia Beach	VA	1550	1400
West Queen Anne	Seattle	WA	2195	1750
Hayward Highland	Hayward	CA	\N	\N
Middlebury	Akron	OH	475	495
Mt. Lookout	Cincinnati	OH	\N	\N
Regent	Town of Madison	WI	\N	995
Roosevelt Park	Grand Rapids	MI	\N	\N
Montclair	Augusta	GA	\N	\N
Heritage Hills	Austin	TX	599	805
Ballast Point	Tampa	FL	1500	1095
Penrose	Saint Louis	MO	\N	595
North Broadway	Cleveland	OH	\N	\N
Deanwood	Washington	DC	\N	\N
Near N Valley	Albuquerque	NM	\N	650
Duclay	Jacksonville	FL	869	813
Childs Park	Saint Petersburg	FL	\N	995
Waterside	Stamford	CT	2275	2275
Old West Tampa	Tampa	FL	\N	995
East Liberty	Pittsburgh	PA	\N	\N
Foothills	Henderson	NV	\N	1200
Fulton	Minneapolis	MN	\N	\N
Knollwood	Kalamazoo	MI	510	2300
Maple High-Six Corners	Springfield	MA	\N	1000
Old West End	Toledo	OH	\N	\N
Sun Groves	Chandler	AZ	\N	1395
Johnston Rd.-McAlpine	Charlotte	NC	921	902
Chinatown	San Francisco	CA	\N	2950
Mt. Hope	San Diego	CA	\N	\N
Manhattan Beach	New York	NY	\N	1900
Merion Village	Columbus	OH	\N	795
Ridgeview-Webster	San Diego	CA	\N	1500
Avondale	Jacksonville	FL	850	995
North Image	Vancouver	WA	\N	965
Penn-Fallsway	Baltimore	MD	\N	\N
Southeast Como	Minneapolis	MN	1180	1875
Jacksonville Farms-Terrace	Jacksonville	FL	1150	1125
Near North	Minneapolis	MN	1100	\N
North Central	Raleigh	NC	750	600
Ashton Heights	Arlington	VA	\N	2395
Marlyville-Fontainebleau	New Orleans	LA	\N	\N
Millbrook	Grand Rapids	MI	\N	\N
North Capitol Hill	Denver	CO	1360	1630
The Greater Ville	Saint Louis	MO	\N	\N
Marshall Heights	Washington	DC	\N	\N
Longfellow	Oakland	CA	1295	\N
Goldsmith	Denver	CO	595	\N
Barton Chapel	Augusta	GA	\N	\N
Highlands	Lincoln	NE	\N	700
Delaware-West Ferry	Buffalo	NY	\N	\N
Bayshore	Miami Beach	FL	\N	2800
Lower South Providence	Providence	RI	\N	\N
East End	Boise	ID	\N	750
Pearl District	Portland	OR	1695	1695
Springs	East Hampton	NY	27000	29000
Branford Center	Branford	CT	1100	975
Normandy Manor	Jacksonville	FL	850	925
Chollas Creek	San Diego	CA	\N	1095
Crossroads	Bellevue	WA	\N	\N
Parkrose Heights	Portland	OR	\N	1200
Newell	Charlotte	NC	870	1000
Homaker Park	Bakersfield	CA	\N	625
Augusta Ranch	Mesa	AZ	1000	1025
South Delridge	Seattle	WA	1070	1200
Side Creek	Aurora	CO	900	\N
Alamo Square	San Francisco	CA	\N	3990
La Sierra Hills	Riverside	CA	\N	\N
Torrey Highlands	San Diego	CA	\N	2600
Mt Eden	Hayward	CA	\N	\N
Smith Hill	Providence	RI	\N	950
Fremont	Oakland	CA	\N	1300
Arlingwood	Jacksonville	FL	\N	875
Marconi Plaza-Packer Park	Philadelphia	PA	\N	\N
Curtis Park	Sacramento	CA	\N	825
Collier Heights	Atlanta	GA	\N	799
Atlanta University Center	Atlanta	GA	\N	\N
Menlo Park	Tucson	AZ	\N	\N
Riverton	Portland	ME	\N	\N
Algonquin	Louisville	KY	\N	600
Parkville	Hartford	CT	800	\N
Rocky Ridge	Aurora	CO	\N	995
John T White	Fort Worth	TX	\N	\N
Windom Park	Minneapolis	MN	\N	1095
Southwest Hills	Portland	OR	2400	\N
Mt. Auburn	Cincinnati	OH	650	795
National Hills	Augusta	GA	585	955
Grand	Riverside	CA	\N	1500
Calhoun	Minneapolis	MN	775	1095
Palm City	San Diego	CA	\N	\N
Arlington Ridge	Arlington	VA	1675	2095
Meydenbauer	Bellevue	WA	960	1700
San Mateo Heights	San Mateo	CA	\N	1695
Downtown West	Minneapolis	MN	950	1395
Meadow Hills	Aurora	CO	995	1295
University Hills	Denver	CO	\N	\N
Pulaski	Detroit	MI	\N	700
Meadow Brook	Oakland	CA	\N	\N
Campus Farm	Tucson	AZ	875	850
South Westnedge	Kalamazoo	MI	\N	\N
People's Freeway	Salt Lake City	UT	\N	\N
La Morada	Stockton	CA	1500	1400
Webster	Oakland	CA	\N	\N
Century City	Los Angeles	CA	2850	3200
West Wood	Dayton	OH	\N	\N
Foxcroft	Charlotte	NC	995	1180
Linden Heights	Dayton	OH	\N	\N
West End	Portland	ME	1150	1295
Watrous South	Des Moines	IA	\N	\N
Highline Villages	Aurora	CO	775	985
West End	Boston	MA	2781	2930
Delano	Wichita	KS	\N	750
South Harrison	Tucson	AZ	\N	1095
San Tan Ranch	Gilbert	AZ	\N	1195
South Semoran	Orlando	FL	695	798
Islandview	Detroit	MI	\N	\N
Oakland Ave-Harrison St	Oakland	CA	1200	1549
Davis Island	Tampa	FL	\N	895
Oceanway	Jacksonville	FL	1100	1250
Marlwood	Charlotte	NC	\N	895
Cherry Creek	Denver	CO	1600	2825
Eastlake	Seattle	WA	\N	1127
Bellevue	Washington	DC	950	\N
Eastgate - Cougar Mountain	Bellevue	WA	\N	1515
Cherokee Point	San Diego	CA	\N	995
Seminary	Oakland	CA	\N	\N
Euclid Green	Cleveland	OH	\N	\N
Adams North	San Diego	CA	\N	1250
Trinidad	Washington	DC	1100	1150
Central Meadowbrook	Fort Worth	TX	\N	\N
Amberwood North	Chandler	AZ	\N	920
Baywood Knolls	San Mateo	CA	\N	2600
Rancho San Antonio	Oakland	CA	\N	\N
Whitehouse	Jacksonville	FL	\N	900
Lakeside Park	Tucson	AZ	\N	950
Fairway-Liberty Heights	Lexington	KY	\N	\N
Venable	Charlottesville	VA	\N	995
Roberts	El Paso	TX	\N	\N
West Loop Gate	Chicago	IL	1575	2000
El Cerrito	San Diego	CA	\N	1495
Totem Lake	Kirkland	WA	1114	1350
Lower Beaver	Des Moines	IA	\N	680
Hiawatha	Minneapolis	MN	1100	\N
Pembroke	Virginia Beach	VA	1330	\N
New Dorp	New York	NY	\N	\N
Windsor Road	Austin	TX	1475	2800
Wexford-Thornapple	Columbus	OH	\N	999
Lake Frendrica	Orlando	FL	686	875
Coral Ridge	Fort Lauderdale	FL	2500	2338
Southcrest	San Diego	CA	\N	\N
Laddie Place and North Wilson	San Antonio	TX	\N	\N
Beaver Hills	New Haven	CT	\N	1300
Southwestern Hills	Des Moines	IA	645	\N
Ednor Gardens-Lakeside	Baltimore	MD	\N	\N
Deep Creek West-Dismal Swamp	Chesapeake	VA	\N	\N
Arcadia Terrace	Chicago	IL	1200	1295
Lynn Lane	Tulsa	OK	\N	1850
Bouldin	Austin	TX	1280	1500
Beacon Hill	San Antonio	TX	\N	575
Maxwell Park	Oakland	CA	\N	\N
Pecan Valley	San Antonio	TX	\N	\N
Lacy	Santa Ana	CA	\N	\N
Montclair	Denver	CO	\N	1000
Platt Park	Denver	CO	\N	1050
Rose Village	Vancouver	WA	\N	\N
Stonehaven	Charlotte	NC	995	\N
Andersonville	Chicago	IL	1250	1550
Settlers Landing	Jacksonville	FL	995	1000
Point Breeze	Pittsburgh	PA	\N	\N
Heights	Little Rock	AR	\N	865
Zilker	Austin	TX	1799	1800
Chambers Heights	Aurora	CO	\N	\N
South Deering	Chicago	IL	\N	1100
City Center North	Aurora	CO	900	\N
Ridgmar	Fort Worth	TX	\N	\N
Glenview	Oakland	CA	\N	\N
Providence Estates East	Charlotte	NC	\N	1550
MIT	Cambridge	MA	2355	2705
North East	Pasadena	CA	1965	\N
South India Mound	Kansas City	MO	\N	\N
Sterling Hills	Aurora	CO	\N	1150
North India Mound	Kansas City	MO	\N	600
Gravois Park	Saint Louis	MO	\N	600
Cedar Park	Seattle	WA	1195	1135
Downer Woods	Milwaukee	WI	\N	\N
Broadway Pantano East	Tucson	AZ	\N	\N
Edmondson Village	Baltimore	MD	\N	1300
Central Bench	Boise	ID	\N	\N
Sorrento Valley	San Diego	CA	\N	2100
Paseo Ranchoero	Chula Vista	CA	\N	\N
Downtown	Saint Petersburg	FL	1599	750
Buckingham	Arlington	VA	\N	1795
Crest Drive	Eugene	OR	\N	\N
Valley	Providence	RI	\N	800
Thomasboro-Hoskins	Charlotte	NC	600	695
Fauntleroy	Seattle	WA	\N	\N
Marshall - Shadeland	Pittsburgh	PA	\N	\N
South Hilltop	Columbus	OH	\N	\N
Braddock Road Metro	Alexandria	VA	1955	2150
City Center	Aurora	CO	769	894
Hayhurst	Portland	OR	\N	\N
Folwell	Minneapolis	MN	1095	\N
Country Club	Lincoln	NE	\N	\N
Riverside	Baltimore	MD	1850	2000
Sweet Briar	Austin	TX	970	1150
Pinehurst	Seattle	WA	\N	1195
Downtown	Sacramento	CA	\N	1700
Washington Heights	Chicago	IL	\N	\N
Starin Central	Buffalo	NY	\N	\N
St. Edwards	Austin	TX	850	1476
Roland Park	Baltimore	MD	\N	\N
Broadmoor	New Orleans	LA	\N	1000
Central Oak Park	Sacramento	CA	\N	995
Countryside Woods	Vancouver	WA	\N	1350
South Main	Houston	TX	905	1115
Edgewood	Washington	DC	\N	1550
Tropico	Glendale	CA	\N	\N
South Park	San Diego	CA	\N	1300
Sheraden	Pittsburgh	PA	\N	\N
Irvington	Baltimore	MD	\N	1100
Kenawood-Rockwood-Hi-Acres-Deep Spring	Lexington	KY	\N	495
Lower Queen Anne	Seattle	WA	1400	1350
Harvard Place - Eastlawn	San Antonio	TX	\N	700
Wooten	Austin	TX	800	1150
Parkland	Louisville	KY	\N	650
South Side CAN	Columbus	OH	550	700
Blue Hills	Kansas City	MO	\N	650
Perris Hills	San Bernardino	CA	\N	\N
East Ridge - Ptarmigan Park	Aurora	CO	790	\N
Woodley Park	Washington	DC	2190	2175
NoHo	New York	NY	3550	3695
Bagley Downs	Vancouver	WA	\N	\N
Myers	Tucson	AZ	\N	\N
Waite Park	Minneapolis	MN	\N	\N
Palo Verde	Tucson	AZ	\N	550
Community Workers Council	San Antonio	TX	\N	\N
Florida Center	Orlando	FL	\N	1850
Patterson Park	Baltimore	MD	1200	1300
North Loop	Austin	TX	1300	1400
Hyde Park	Austin	TX	1400	1275
Central Business District	Newark	NJ	1550	1700
Near East Side	Chicago	IL	1882	2225
Marble Cliff Crossing	Columbus	OH	890	\N
Mission Hills	San Diego	CA	\N	1750
Central Clintonville	Columbus	OH	\N	\N
Fruitridge Manor	Sacramento	CA	\N	\N
Midtown	Saint Louis	MO	\N	\N
Longfellow	Minneapolis	MN	\N	\N
Horseshoe Park	Aurora	CO	\N	1200
Beaumont-Wilshire	Portland	OR	\N	\N
Old Savannah	Augusta	GA	\N	700
Presidential Park	Riverside	CA	\N	\N
Victory Heights	Seattle	WA	\N	1195
Columbia Forest	Arlington	VA	\N	1550
Eastown	Grand Rapids	MI	\N	1300
Woodrow	New York	NY	\N	1300
Alameda	Portland	OR	\N	\N
Milan	New Orleans	LA	\N	\N
Julia Keen	Tucson	AZ	\N	\N
North Hilltop	Columbus	OH	\N	\N
Hickory Grove	Charlotte	NC	895	795
Belle Vista	Youngstown	OH	\N	\N
Vine	Kalamazoo	MI	\N	900
Lynwood Hills	Chula Vista	CA	\N	\N
Hagginwood	Sacramento	CA	\N	900
Loma Portal	San Diego	CA	\N	\N
Shandin Hills	San Bernardino	CA	900	995
Pepperidge	Augusta	GA	\N	\N
Central	Raleigh	NC	1085	700
Astoria Heights	New York	NY	\N	2200
Arlington-East Falls	Arlington	VA	\N	2796
Olde Providence South	Charlotte	NC	1250	\N
Westside	Missoula	MT	750	900
Seville	Gilbert	AZ	\N	1500
Leawood	Columbus	OH	\N	675
Rosedale	Austin	TX	1350	1635
Groves Lincoln Park	Tucson	AZ	\N	850
Keeling	Tucson	AZ	\N	575
Klondike	Louisville	KY	\N	\N
Westerleigh	New York	NY	\N	\N
Chevy Chase-Ashland Park	Lexington	KY	\N	\N
Holliswood	New York	NY	1200	1400
Galt Mile	Fort Lauderdale	FL	2400	1800
Georgia Tech	Atlanta	GA	1039	\N
Upton	Baltimore	MD	900	\N
Business District	Irvine	CA	1812	2250
Idlewild Farms	Charlotte	NC	\N	\N
University Hills	Los Angeles	CA	\N	950
Bayside	Everett	WA	\N	1000
Arroyo Viejo	Oakland	CA	\N	\N
Puget	Bellingham	WA	\N	\N
Belknap Lookout	Grand Rapids	MI	\N	795
Riverdale	Detroit	MI	750	750
Fairgrounds	New Orleans	LA	\N	\N
North Tabor	Portland	OR	\N	825
Sans Souci	Jacksonville	FL	683	\N
Mallard Creek - Withrow Downs	Charlotte	NC	\N	1275
Kings Point	Great Neck	NY	\N	\N
Summer Place Village	Mesa	AZ	\N	900
Bolton Hill	Baltimore	MD	\N	\N
Country Club	Stockton	CA	\N	995
Los Cerritos Area	Long Beach	CA	\N	\N
Regent Park	Detroit	MI	\N	700
Highland Park	Augusta	GA	\N	\N
Leschi	Seattle	WA	\N	1550
Laurelhurst	Seattle	WA	\N	895
Mount Vernon	Baltimore	MD	1165	1009
Memorial Square	Springfield	MA	\N	\N
Arcadia	Kalamazoo	MI	600	1396
Harmony	Fort Worth	TX	\N	\N
Lyon Park	Arlington	VA	1900	1910
Midtown	Anchorage	AK	\N	\N
Highland Terrace	Richardson	TX	\N	\N
Coral Ridge Country Club	Fort Lauderdale	FL	1700	1400
O'Fallon	Saint Louis	MO	\N	575
Spring Valley	Washington	DC	\N	\N
Webber-Camden	Minneapolis	MN	\N	950
Mesa Grande	Mesa	AZ	795	795
Fox Point	Providence	RI	950	1250
The Provinces	Chandler	AZ	1150	1225
Northwest Everett	Everett	WA	\N	\N
Stone Meadows	Bakersfield	CA	\N	1500
Sherwood Forest	Jacksonville	FL	\N	895
Roxhill	Seattle	WA	\N	\N
Oak Tree	Oakland	CA	\N	\N
North Heights	Youngstown	OH	\N	500
Burbank	Hayward	CA	\N	\N
McGirts Creek	Jacksonville	FL	\N	1050
The North End	Virginia Beach	VA	1400	1975
Windom	Minneapolis	MN	675	\N
West Gate	Toledo	OH	\N	\N
Central Business District	Cincinnati	OH	975	1450
Bloomingdale	Washington	DC	\N	2500
Becton Park	Charlotte	NC	698	\N
Bluff Heights	Long Beach	CA	\N	1250
Kerns	Portland	OR	\N	1195
Timmerman West	Milwaukee	WI	\N	\N
Belltown	Stamford	CT	\N	1850
Northside	Kalamazoo	MI	\N	\N
North Central	San Mateo	CA	\N	\N
Juneau Town	Milwaukee	WI	1300	1200
Baden	Saint Louis	MO	\N	\N
Jacobs	Louisville	KY	\N	550
Sarritt Point	Kansas City	MO	465	575
Hot Wells	San Antonio	TX	\N	\N
Marina	San Diego	CA	1795	2095
Chugiak	Anchorage	AK	\N	1695
Upper B Street	Hayward	CA	\N	\N
Audubon Park	Minneapolis	MN	\N	\N
Derita-Statesville	Charlotte	NC	\N	975
Gorgas	Mobile	AL	\N	\N
Northpoint	Milwaukee	WI	\N	\N
Bashford Manor	Louisville	KY	\N	639
Woodlawn	Portland	OR	\N	\N
Lansdowne	Charlotte	NC	863	825
Colonial Heights	Stockton	CA	\N	\N
Walnut Hills	Dayton	OH	\N	\N
Aggasiz - Harvard North	Cambridge	MA	1595	2085
Hamey Heights	Vancouver	WA	\N	800
Washington Park	Milwaukee	WI	\N	\N
Barney Circle	Washington	DC	\N	\N
Dorsey-Riverbend	Fort Lauderdale	FL	1350	1195
East Shore	New Haven	CT	\N	1195
Boyle Park	Little Rock	AR	\N	800
Lakeshore	San Francisco	CA	2375	\N
South Central Hilltop	Columbus	OH	\N	675
Marquette	Town of Madison	WI	\N	1150
Whitman-Mocine	Hayward	CA	\N	\N
Eastway-Sheffield Park	Charlotte	NC	675	680
Parnassus - Ashbury	San Francisco	CA	\N	2895
Virginia Park	Tampa	FL	\N	\N
Fairmount Park	Seattle	WA	\N	1235
San Mateo Village	San Mateo	CA	\N	\N
SWAN	Grand Rapids	MI	\N	975
Shore Acres	Saint Petersburg	FL	\N	1100
Feldheym	San Bernardino	CA	\N	650
La Plaza	San Bernardino	CA	\N	900
Evergreen	Everett	WA	\N	\N
Whittier	Boulder	CO	1595	1900
Allendale	Oakland	CA	\N	\N
Terra Del Sol	Tucson	AZ	\N	875
Riverbend	Tampa	FL	\N	\N
Campbellton Road	Atlanta	GA	\N	500
Birchwood	Bellingham	WA	\N	615
Fairlane	Kansas City	MO	\N	875
Lansingville	Youngstown	OH	\N	\N
University	Syracuse	NY	\N	\N
Shippan	Stamford	CT	\N	3000
Whittier Heights	Seattle	WA	\N	\N
Bolton	Mobile	AL	675	\N
City Park West	Denver	CO	\N	1170
Ashcreek	Portland	OR	\N	\N
Tower Homes	Kansas City	MO	\N	\N
Phillips West	Minneapolis	MN	\N	\N
Whittier	Denver	CO	\N	\N
Fort Sanders	Knoxville	TN	675	595
Yerba Buena	San Francisco	CA	2600	3564
Van Mall	Vancouver	WA	\N	871
Park View	Washington	DC	\N	1250
Roseville - Fleet Ridge	San Diego	CA	\N	\N
Arlington	Jacksonville	FL	\N	830
College Hill	Wichita	KS	\N	\N
Big Oaks	Chicago	IL	\N	\N
Jefferson-Woodlawn Lake	San Antonio	TX	\N	\N
Arlington Heights	Fort Worth	TX	\N	925
Millsmont	Oakland	CA	\N	1300
Baker	Denver	CO	1900	1765
Kennedy Heights	Cincinnati	OH	\N	\N
The Seasons	Bakersfield	CA	\N	\N
Riverside	Everett	WA	\N	\N
Canaryville	Chicago	IL	\N	1000
Wesconnett	Jacksonville	FL	\N	750
Midtown Phillips	Minneapolis	MN	\N	1175
New Northwood	Baltimore	MD	\N	\N
Rose Park	Missoula	MT	\N	795
North University	Austin	TX	1100	1435
Stella Mann	Tucson	AZ	\N	839
West Chatham	Chicago	IL	\N	1250
University District	Minneapolis	MN	\N	\N
Brooklyn	Portland	OR	\N	925
Manito-Cannon Hill	Spokane	WA	\N	\N
West Riverside	New Orleans	LA	\N	1350
Binz	Houston	TX	2055	1700
Wakefield	Tucson	AZ	\N	595
Upper Boggy Creek	Austin	TX	1050	1150
Atlantic Boulevard Estates	Jacksonville	FL	800	\N
Barclay Downs	Charlotte	NC	1150	1400
Clifton Heights	Louisville	KY	635	\N
Grove Park	Atlanta	GA	\N	800
Humboldt	Portland	OR	\N	\N
Summer Valley	Aurora	CO	\N	\N
North East Park	Saint Petersburg	FL	\N	775
Ellsworth Springs	Vancouver	WA	\N	\N
Seccombe Lane	San Bernardino	CA	\N	695
Downtown	Lincoln	NE	\N	\N
Park Shore	Naples	FL	3000	6000
Chollas View	San Diego	CA	\N	\N
Randall Manor	New York	NY	\N	\N
Nauck	Arlington	VA	2179	1951
Iroquois	Louisville	KY	\N	\N
Eastern Hills	Dayton	OH	\N	\N
Laurelhurst	Portland	OR	\N	\N
South Addition	Anchorage	AK	\N	1800
South Oak Park	Sacramento	CA	\N	\N
Downtown Neighborhood	Little Rock	AR	\N	\N
Pecan Springs Springdale	Austin	TX	\N	\N
Morrell Park	Baltimore	MD	\N	\N
Cascade View	Everett	WA	\N	\N
Irving Woods	Chicago	IL	\N	\N
Broadway East	Baltimore	MD	950	1000
Pettit-Rudisill	Fort Wayne	IN	\N	500
Sonterra-Stone Oak	San Antonio	TX	\N	\N
McKnight	Springfield	MA	\N	1000
Village 11	Sacramento	CA	\N	1475
Cross Country	Baltimore	MD	\N	\N
Country Club Heights	Charlotte	NC	\N	\N
Garment District	New York	NY	2750	3300
Madrona	Torrance	CA	\N	\N
Arlington South	Riverside	CA	\N	\N
Grand Lake	Oakland	CA	1195	\N
Duck Creek	Richardson	TX	1035	\N
Walteria	Torrance	CA	\N	\N
University Hills	Austin	TX	930	\N
Prescott	Oakland	CA	\N	\N
Buckingham Lake - Crestwood	Albany	NY	\N	\N
Lake Lucina	Jacksonville	FL	680	759
Wenonah	Minneapolis	MN	\N	\N
Cole	Denver	CO	\N	\N
Bixby Knolls	Long Beach	CA	\N	975
Victory	Minneapolis	MN	\N	1100
Downtown	Detroit	MI	1460	\N
Cobblestone	Jacksonville	FL	899	\N
Marina Area	Long Beach	CA	\N	2495
Lakeshore	Oakland	CA	\N	1495
Parkhill	Mobile	AL	\N	900
Lind-Bohanon	Minneapolis	MN	899	1150
Downtown Jacksonville	Jacksonville	FL	1250	1150
Northeast Hillsdale	San Mateo	CA	\N	\N
Overton South	Fort Worth	TX	\N	\N
South Hill	Bellingham	WA	\N	\N
The Oaks	Bakersfield	CA	\N	1200
Mission Bay	San Francisco	CA	\N	3846
Bryant	Seattle	WA	\N	\N
Donaldson Terrace	San Antonio	TX	\N	650
Bomber Heights	Fort Worth	TX	\N	\N
Belmont	Lincoln	NE	\N	\N
Cory Lake Isles	Tampa	FL	\N	2000
California	Louisville	KY	\N	725
Olde Town East	Columbus	OH	\N	550
Oxford Hunt	Charlotte	NC	766	\N
North Central Thousand Oaks	San Antonio	TX	\N	1150
East Atlanta	Atlanta	GA	1250	1295
Bayside West	Tampa	FL	924	1000
Mt. Baker	Bellingham	WA	879	\N
Roosevelt	Seattle	WA	\N	\N
Mount Pleasant	Saint Louis	MO	\N	500
Westlake	Seattle	WA	1245	1670
Greater Belhaven	Jackson	MS	\N	\N
Alta Mesa	Santa Barbara	CA	\N	\N
Lykins	Kansas City	MO	\N	500
San Gorgonio	San Bernardino	CA	\N	\N
Wildwood Park	San Bernardino	CA	\N	1350
Loch Raven	Baltimore	MD	900	\N
Old North Sacramento	Sacramento	CA	\N	750
South Hagginwood	Sacramento	CA	\N	895
North Loop	Minneapolis	MN	1495	1695
Lakewood	Jacksonville	FL	900	1025
Bird Land	San Diego	CA	\N	\N
Kelvin Park	Chicago	IL	\N	\N
Alban Hills	Albuquerque	NM	\N	\N
Landover Sharmel	Vancouver	WA	\N	1005
East End	Portland	ME	1195	1650
Lakeland	Baltimore	MD	950	1100
Southside Slopes	Pittsburgh	PA	\N	1575
Pioneer Park	Des Moines	IA	585	\N
North Wyoming	Albuquerque	NM	\N	\N
Northwest Heights	Portland	OR	1295	2500
Palma Ceia	Tampa	FL	1150	1350
Highland	Austin	TX	990	900
Lincoln Square	Chicago	IL	1100	1345
Spring Park	Jacksonville	FL	\N	750
South Park	Des Moines	IA	\N	\N
Teralta West	San Diego	CA	\N	\N
Minnetex	Houston	TX	\N	\N
Downtown	Providence	RI	1525	2095
South Amherst	Amherst	MA	\N	\N
Merritt	Oakland	CA	\N	\N
Anacostia	Washington	DC	\N	\N
Moose Can Gully	Missoula	MT	\N	\N
Biscayne Point	Miami Beach	FL	\N	1600
Seaview	Seattle	WA	\N	\N
Central Lawrenceville	Pittsburgh	PA	765	1350
Holland	Minneapolis	MN	\N	1000
Brightwood	Springfield	MA	\N	925
Swan Canyon	San Diego	CA	\N	1050
Downtown West	Saint Louis	MO	980	1365
Victorian Village	Columbus	OH	\N	1300
South East End	Grand Rapids	MI	\N	\N
Twenty-Fifth Ave	San Mateo	CA	\N	\N
SableRidge	Aurora	CO	\N	\N
Miraloma Park	San Francisco	CA	\N	\N
Regency	Jacksonville	FL	900	895
Wakefield	Little Rock	AR	\N	675
Harlem Park	Baltimore	MD	\N	825
South Fairmount	Cincinnati	OH	\N	725
Crystal Lake	Lakeland	FL	\N	\N
Malibar Heights	Mobile	AL	\N	\N
Prospect Hill	New Haven	CT	\N	900
Harwood Lane	Charlotte	NC	975	1095
Ogden	Vancouver	WA	\N	853
Homan Square	Chicago	IL	\N	900
Weibel	Fremont	CA	\N	\N
Goodrich-Kirkland Park	Cleveland	OH	\N	\N
Rolling Hills	Jacksonville	FL	\N	\N
Mission Beach	San Diego	CA	1800	3300
Mount Vernon-Hollywood-Montclair	Lexington	KY	\N	\N
Belmont	Charlottesville	VA	875	850
Argyle Forest	Jacksonville	FL	960	1000
Willowcreek	Sacramento	CA	\N	1495
Mckinley Mitchell	Tulsa	OK	\N	\N
Cotswold	Charlotte	NC	725	850
Summerville	Augusta	GA	\N	750
Interbay	Seattle	WA	\N	1601
Old West Austin	Austin	TX	1700	1975
Alessandro	San Bernardino	CA	\N	\N
Wesley Heights	Washington	DC	2200	2200
Lafayette Park	Detroit	MI	726	\N
Meadow Creek	Fort Worth	TX	\N	1195
Skinker-DeBaliviere	Saint Louis	MO	\N	1050
Edgebrook	Chicago	IL	\N	\N
Adams Hill	San Antonio	TX	\N	\N
Port Tampa City	Tampa	FL	2029	1199
Martin Park	Detroit	MI	\N	750
Nob Hill	Albuquerque	NM	\N	725
Overton	Mobile	AL	\N	\N
Ridgeway	Stamford	CT	\N	2450
Lindridge - Martin Manor	Atlanta	GA	1075	1501
Harbour Island	Tampa	FL	1700	1850
McClure Park	Tulsa	OK	\N	\N
Sylvan Hills	Atlanta	GA	\N	750
Como	Fort Worth	TX	\N	\N
Edgewood	New Haven	CT	\N	875
Rockwood	Spokane	WA	\N	\N
Central Business District	Rochester	NY	895	\N
Amity	New Haven	CT	\N	900
Riviera - Westchester	Bakersfield	CA	\N	795
Ginter Park	Richmond	VA	\N	600
Woodstock	Jacksonville	FL	650	715
Midtown	San Diego	CA	\N	2295
Uptown	Seattle	WA	1500	1621
West End	Atlanta	GA	900	800
Monte Vista	San Antonio	TX	\N	850
Ybor City	Tampa	FL	\N	950
Central East Austin	Austin	TX	1325	1593
Terrace Hills	Mobile	AL	765	\N
MLK	Austin	TX	1200	\N
Downtown	Saint Louis	MO	1025	1500
The Gables	Columbus	OH	\N	\N
South End	Springfield	MA	885	941
Davis Lake - Eastfield	Charlotte	NC	1100	1000
Village 9	Sacramento	CA	\N	1495
Rosewood	Austin	TX	1260	\N
Kennedy	Denver	CO	765	\N
Briarcreek-Woodland	Charlotte	NC	675	995
Holly Grove	New Orleans	LA	\N	\N
Garden Acres	Fort Worth	TX	\N	1150
Charlotte Park	Nashville	TN	\N	\N
Far Southwest	Fort Worth	TX	\N	1150
Manton	Providence	RI	\N	\N
Hawthorne	Minneapolis	MN	950	1150
Dauphin Acres	Mobile	AL	\N	575
North Riverside	Wichita	KS	\N	\N
West Chesterfield	Chicago	IL	\N	\N
Mission San Jose	San Antonio	TX	669	\N
Timber Ridge	San Antonio	TX	\N	\N
Oxford	Fort Wayne	IN	\N	\N
Fieldston	New York	NY	1690	1595
Platinum Triangle	Anaheim	CA	1770	1950
Clayton	Denver	CO	\N	\N
East English Village	Detroit	MI	\N	800
Hoover-Foster	Oakland	CA	\N	\N
Yorkwood	Mobile	AL	\N	\N
Tenney-Lapham	Town of Madison	WI	\N	1150
West	Helena	MT	\N	650
North Kenwood	Chicago	IL	\N	1375
Madison Park	Charlotte	NC	1250	1400
Little Turtle	Columbus	OH	\N	770
Santa Clara	Eugene	OR	\N	\N
Fells Point	Baltimore	MD	1964	2210
Shandon	Columbia	SC	\N	895
Bridlemile	Portland	OR	\N	\N
Sunset Heights	Milwaukee	WI	\N	\N
Madison Park	Seattle	WA	\N	\N
Rockwell Park-Hemphill Heights	Charlotte	NC	900	995
Jefferson Park	Charlottesville	VA	\N	1100
Stockton	San Diego	CA	\N	\N
Ellwanger-Barry	Rochester	NY	\N	900
Northwood Point	Irvine	CA	2995	2775
Fallstaff	Baltimore	MD	\N	\N
Emerald Hills	San Diego	CA	\N	\N
University Gardens	Great Neck	NY	\N	3295
North Riverdale	Dayton	OH	\N	550
View Ridge	Seattle	WA	\N	1350
Banksville	Pittsburgh	PA	\N	\N
East Westwood	Cincinnati	OH	\N	\N
East Carollton	New Orleans	LA	\N	1100
Old Hill	Springfield	MA	\N	\N
Fairoaks	Tampa	FL	1050	925
Berkleigh	Mobile	AL	\N	\N
Streeterville	Chicago	IL	1600	2055
Wallhaven	Akron	OH	\N	\N
Union Station	Denver	CO	1635	2500
Apollo Arapaho & Camelot	Garland	TX	\N	\N
East Merrimack	Merrimack	NH	\N	\N
Lytle Creek	San Bernardino	CA	\N	\N
Sardis Woods	Charlotte	NC	\N	\N
Tower Triangle	Aurora	CO	\N	\N
Dongan Hills	New York	NY	\N	\N
Oakland	Chicago	IL	\N	1250
Zach White	El Paso	TX	\N	\N
Lakeshore	Jacksonville	FL	\N	\N
Reed	Portland	OR	\N	\N
Del Paso Heights	Sacramento	CA	\N	\N
Tallyn's Reach	Aurora	CO	\N	1285
College Park	Mobile	AL	\N	\N
East Phillips	Minneapolis	MN	\N	\N
Hancock	Austin	TX	1195	1500
Temescal	Oakland	CA	\N	\N
White Ash	Columbus	OH	\N	1250
Far West	Eugene	OR	\N	630
Western Hills North	Fort Worth	TX	\N	765
Presidio Heights	San Francisco	CA	\N	3850
Maryvale	Mobile	AL	\N	750
Roosevelt	Toledo	OH	\N	\N
Kendall	San Bernardino	CA	\N	\N
Route 66 West	Albuquerque	NM	\N	\N
Rancho San Joaquin	Irvine	CA	1900	\N
Sam Hughes	Tucson	AZ	\N	935
Shelltown	San Diego	CA	\N	\N
Downtown	Tulsa	OK	\N	\N
Belcaro	Denver	CO	1558	1994
North City Farms	Sacramento	CA	\N	\N
Kilbourn Town	Milwaukee	WI	1733	\N
Hartwell	Cincinnati	OH	\N	\N
West Eugene	Eugene	OR	\N	\N
Elizabeth	Charlotte	NC	895	995
Treme' Lafitte	New Orleans	LA	\N	900
Dexter Falls	Columbus	OH	1048	\N
City Center	Miami Beach	FL	\N	3500
West Rock	New Haven	CT	\N	\N
Eastside	Tucson	AZ	\N	1100
Phoenix Hill	Louisville	KY	\N	800
City Island	New York	NY	\N	1700
Belknap	Louisville	KY	\N	\N
Peachtree Heights West	Atlanta	GA	1280	1195
Tevis Ranch	Bakersfield	CA	\N	\N
Barelas	Albuquerque	NM	\N	\N
Sabin	Portland	OR	\N	\N
Driving Park	Columbus	OH	\N	550
Sequoyah	Tulsa	OK	\N	\N
Nob Este	Albuquerque	NM	\N	\N
International	San Bernardino	CA	\N	\N
Chosewood Park	Atlanta	GA	\N	750
Highland Terrace	Oakland	CA	\N	\N
Central Business District	Louisville	KY	620	1395
Kranz Woods	Detroit	MI	\N	\N
Martin Acres	Boulder	CO	2500	2460
University City South	Charlotte	NC	\N	\N
Table Mesa South	Boulder	CO	\N	\N
Longview Lake	Tulsa	OK	\N	\N
Benton Park West	Saint Louis	MO	\N	650
Fulton	Richmond	VA	599	882
Norkirk	Kirkland	WA	\N	\N
Tobin Hill	San Antonio	TX	\N	1200
Cahuenga Pass	Los Angeles	CA	4300	4000
Arrowhead	Jacksonville	FL	825	\N
Park of the Canals	Mesa	AZ	\N	975
Downtown	Oakland	CA	\N	\N
Hillcrest	Boise	ID	555	750
Mission Hills	Henderson	NV	1050	1050
Isle of Palms	Jacksonville	FL	879	\N
Closeburn-Glenkirk	Charlotte	NC	1040	1195
Glenrose Heights	Atlanta	GA	731	773
Southwest Garden	Saint Louis	MO	\N	795
Downtown	Washington	DC	2542	2800
Indianola Terrace	Columbus	OH	\N	875
Arlington Manor	Jacksonville	FL	\N	\N
Lindbergh	Atlanta	GA	1025	1350
Deering Center	Portland	ME	\N	\N
Mid-Town Belvedere	Baltimore	MD	1467	1250
West Side	Augusta	GA	\N	790
East Hampton North	East Hampton	NY	37000	38000
Perry South	Pittsburgh	PA	\N	\N
North Shoal Creek	Austin	TX	899	995
Summit Lake	Akron	OH	\N	675
Casablanca	Riverside	CA	\N	\N
VCU	Richmond	VA	\N	\N
Terra Nova	Chula Vista	CA	\N	\N
Financial District	San Francisco	CA	2235	3500
Bowmanville	Chicago	IL	1195	1315
Wayne State	Detroit	MI	\N	\N
Nevin Community	Charlotte	NC	\N	\N
Goodby's Creek	Jacksonville	FL	895	\N
Melrose Manors	Fort Lauderdale	FL	1700	1500
Garden Springs	Lexington	KY	\N	\N
Murray Hill	Milwaukee	WI	995	999
Westbranch	Houston	TX	1024	\N
Spectrum	Gilbert	AZ	\N	1295
Mark Twain	Saint Louis	MO	\N	\N
Ryanwood	Fort Worth	TX	\N	\N
Beach Park	Tampa	FL	1249	1650
Interlake	Bellevue	WA	\N	\N
The Cape	Jacksonville	FL	1325	1395
McElderry Park	Baltimore	MD	1000	1100
Riverview	Jacksonville	FL	\N	795
Tollgate Overlook	Aurora	CO	\N	\N
Hartley	Lincoln	NE	\N	\N
Sequoyah	Oakland	CA	\N	\N
Wyandotte	Louisville	KY	\N	\N
Bergen Beach	New York	NY	\N	1350
Woodward Park	Columbus	OH	\N	\N
North Hayward	Hayward	CA	\N	\N
Horner Park	Chicago	IL	1015	\N
Central Beach Alliance	Fort Lauderdale	FL	1950	1900
Dineen Park	Milwaukee	WI	\N	\N
South Seminole Heights	Tampa	FL	\N	950
Downtown	Stockton	CA	\N	\N
Alger Heights	Grand Rapids	MI	\N	\N
Holden Heights	Orlando	FL	\N	\N
Berg-Lasher	Detroit	MI	\N	725
Downtown	Fort Lauderdale	FL	1950	2550
Meredith	Des Moines	IA	\N	\N
Ventura	Orlando	FL	\N	795
Ruskin Heights	Kansas City	MO	\N	725
Birmingham	Toledo	OH	\N	\N
Escalante	Tempe	AZ	825	995
Woodbury	Glendale	CA	\N	\N
Covell Park	Davis	CA	\N	\N
Greenwood & Hamilton	Trenton	NJ	\N	\N
Dam East-West	Aurora	CO	\N	\N
West River	New Haven	CT	\N	\N
Upper Land Park	Sacramento	CA	\N	\N
Sharon Woods	Charlotte	NC	795	975
East Del Paso Heights	Sacramento	CA	\N	\N
East Community Team South	Kansas City	MO	\N	\N
North Oak Park	Sacramento	CA	\N	795
Coronado Ranch	Gilbert	AZ	\N	\N
Macons Corner	Virginia Beach	VA	\N	\N
Fourth Ward	Houston	TX	1020	2400
River Road	Eugene	OR	\N	\N
Oakford Park	Tampa	FL	\N	600
Cory - Merrill	Denver	CO	\N	\N
Galveston	Chandler	AZ	\N	\N
Sunland Village	Mesa	AZ	\N	\N
Crestview	Austin	TX	1000	1501
Pecan Park	Jacksonville	FL	\N	1400
Fairmount	Fort Worth	TX	\N	1095
Mayfair	Washington	DC	\N	\N
Oliver	Baltimore	MD	\N	1150
Parkview Hills	Fort Worth	TX	\N	1200
Lauraville	Baltimore	MD	\N	\N
Charter Point	Jacksonville	FL	669	\N
South Broadway	Albuquerque	NM	\N	\N
South Louisville	Louisville	KY	\N	\N
Ladera West	Albuquerque	NM	\N	\N
East Beverly	Chicago	IL	\N	\N
Goose Island	Chicago	IL	1750	2200
North Stonehurst	Oakland	CA	\N	1250
Park Duvalle	Louisville	KY	\N	\N
River Trails	Fort Worth	TX	\N	\N
Tallulah - North Shore	Jacksonville	FL	\N	800
Schenk-Atwood	Town of Madison	WI	\N	\N
South East Community	Grand Rapids	MI	\N	700
Penrose	Arlington	VA	1825	1655
Sehome	Bellingham	WA	\N	\N
Downtown	Trenton	NJ	\N	\N
Fairmount	Eugene	OR	\N	\N
Eckington	Washington	DC	2397	\N
Harrington	Oakland	CA	\N	\N
Wright View	Dayton	OH	\N	\N
Old Norwood Park	Chicago	IL	\N	\N
Tower Heights	Tulsa	OK	\N	\N
Northeast	South Bend	IN	\N	\N
Forest Hills Gardens	New York	NY	2500	2795
Central	Seattle	WA	\N	\N
Burkhardt	Dayton	OH	\N	\N
Corcoran	Minneapolis	MN	\N	\N
Coquina Key	Saint Petersburg	FL	900	1100
Kleinman Park	Mesa	AZ	\N	\N
South Westside	Olympia	WA	\N	\N
West Minnehaha	Vancouver	WA	\N	\N
Wescott	Syracuse	NY	\N	\N
Port Ivory	New York	NY	\N	\N
Pawtuckett	Charlotte	NC	\N	\N
Magnolia Gardens	Jacksonville	FL	\N	775
Fourth Ward	Charlotte	NC	1099	1409
Woodstone	San Antonio	TX	\N	1000
Mount Washington	Baltimore	MD	\N	\N
Madison Valley	Seattle	WA	1850	\N
Milkhouse	Mobile	AL	\N	\N
Midtown	Grand Rapids	MI	\N	900
Southmoor Park	Denver	CO	1030	1265
Carrollton Ridge	Baltimore	MD	\N	895
Lathrop Homes	Chicago	IL	1950	1800
Nashboro Village	Nashville	TN	712	\N
Long Branch Creek	Arlington	VA	1880	2000
Ormewood Park	Atlanta	GA	1350	1395
Greensbriar	Detroit	MI	\N	700
Reichlieu	Mobile	AL	\N	795
Sandpointe	Santa Ana	CA	\N	\N
West Plaza	Kansas City	MO	895	950
Northgate	Sacramento	CA	\N	\N
Oakland-Winchell	Kalamazoo	MI	\N	\N
45th and Moncrief	Jacksonville	FL	\N	775
Westside Development	Tucson	AZ	\N	\N
Greenbriar	Atlanta	GA	\N	\N
Lowry Hill	Minneapolis	MN	1749	1275
East Columbus	Columbus	OH	\N	\N
Rum Village	South Bend	IN	\N	650
Southmoreland	Kansas City	MO	695	750
Cajon	San Bernardino	CA	\N	1350
West Portland Park	Portland	OR	\N	\N
Greenwood Hills	Richardson	TX	\N	\N
Downtown	Albuquerque	NM	\N	695
Azalea-Hollywood Park	San Diego	CA	\N	\N
Mountain View	Vancouver	WA	\N	\N
Stevens Square	Minneapolis	MN	675	720
Bryn Mawr	Orlando	FL	\N	995
Cooper Commons	Chandler	AZ	1200	1195
Whiteaker	Eugene	OR	\N	595
Candleridge	Fort Worth	TX	\N	\N
Stapleton	Denver	CO	1352	1795
Centretech	Aurora	CO	\N	1051
Near Northwest	South Bend	IN	\N	645
Downtown	Baltimore	MD	1300	1625
Cherokee Triangle	Louisville	KY	\N	1250
French Quarter	New Orleans	LA	1575	2250
Allendale	Baltimore	MD	\N	1150
Edgewood	Atlanta	GA	\N	1200
Lyon Village	Arlington	VA	2600	2050
Rickarby	Mobile	AL	\N	650
Southwest Airport	Columbus	OH	705	\N
Madrona	Seattle	WA	\N	\N
Core City	Detroit	MI	\N	\N
Riverside Rancho	Glendale	CA	\N	\N
Salem Village	Columbus	OH	\N	\N
Mondawin	Baltimore	MD	\N	\N
Greenway	Washington	DC	\N	\N
Inman Park	Atlanta	GA	1465	1748
Carlen	Mobile	AL	\N	650
WoodRidge	Bellevue	WA	\N	\N
Douglas Park	Chicago	IL	\N	\N
Beechfield	Baltimore	MD	\N	\N
Oak Park	Stockton	CA	\N	\N
Grand Park	Jacksonville	FL	\N	\N
Ridglea North	Fort Worth	TX	\N	1209
Corona Heights	San Francisco	CA	\N	2899
Ocean Avenue	Portland	ME	1050	\N
Magnolia Glen	Chicago	IL	780	1000
Middle River Terrace	Fort Lauderdale	FL	1349	1175
Riverside	Spokane	WA	\N	\N
Miramonte	Tucson	AZ	799	535
Playa Vista	Los Angeles	CA	2800	2900
Northgate	Colorado Springs	CO	1049	\N
Heather Ridge	Aurora	CO	\N	\N
West Downtown	Santa Barbara	CA	\N	1600
S.R. Marmon	Albuquerque	NM	\N	\N
Glenwood Meadows	Sacramento	CA	\N	\N
Village 7	Sacramento	CA	\N	\N
Eastland Park-Dixie Plantation	Lexington	KY	\N	\N
Underwood Hills	Atlanta	GA	950	\N
Hickman Mills	Kansas City	MO	\N	825
Venetian Hills	Atlanta	GA	\N	900
Griers Fork	Charlotte	NC	\N	\N
South Park	Tucson	AZ	\N	\N
Volker	Kansas City	MO	599	650
Berea	Baltimore	MD	\N	1000
Park	Detroit	MI	\N	800
Turner Park	Tulsa	OK	\N	900
Glacier View	Everett	WA	\N	\N
Eagle Lake	Charlotte	NC	\N	\N
Shady Oaks	San Antonio	TX	\N	\N
Tulane-Gravier	New Orleans	LA	\N	\N
U Street Corridor	Washington	DC	2445	2575
Globeville	Denver	CO	\N	\N
Oakland City	Atlanta	GA	\N	800
Garden Hills	Atlanta	GA	1675	1740
Saint Mary's	Long Beach	CA	\N	\N
Iveywood	Oakland	CA	\N	\N
North Delridge	Seattle	WA	\N	\N
Ranch Triangle	Chicago	IL	1950	2160
East Hills	Grand Rapids	MI	\N	1350
Glenfair	Portland	OR	\N	\N
Park Hill	Louisville	KY	\N	575
Creekside	Sacramento	CA	\N	1500
Central Business District	Denver	CO	1695	2800
East Harriet	Minneapolis	MN	\N	\N
Fulton River District	Chicago	IL	1718	2035
Eisenhower East	Alexandria	VA	2100	2250
LaSalle College Park	Detroit	MI	\N	700
East Deering	Portland	ME	\N	\N
Whitman	Spokane	WA	\N	\N
Lincoln	Vancouver	WA	\N	\N
Central Business District	Orlando	FL	1160	1450
Eastwood Hill East	Kansas City	MO	\N	800
Barcroft	Arlington	VA	\N	\N
Camelot	Garland	TX	\N	\N
West Central	Fort Wayne	IN	\N	425
Kingsway East	Saint Louis	MO	\N	\N
Bayou St. John	New Orleans	LA	\N	\N
Meadowbrook	Seattle	WA	\N	\N
Confederate Point	Jacksonville	FL	\N	\N
John Ball Park	Grand Rapids	MI	\N	1700
Ellwood Park-Monument	Baltimore	MD	\N	1100
Benton Park	Saint Louis	MO	\N	875
Moss Bay	Kirkland	WA	1590	1933
Oak Center	Oakland	CA	\N	\N
Holly	Austin	TX	1250	\N
Northrich	Richardson	TX	\N	1500
East Congress	Austin	TX	992	1345
UMC	Las Vegas	NV	\N	895
Westside	South Bend	IN	\N	565
Hope	Santa Barbara	CA	\N	\N
Riverland	Fort Lauderdale	FL	\N	1300
Town Center	Reston	VA	\N	\N
New Village	Phoenix	AZ	\N	\N
Columbia Street Waterfront District	New York	NY	2100	2600
Central Business District	Pittsburgh	PA	1565	1495
Mission Hills	El Paso	TX	\N	1200
Morris Heights	Aurora	CO	\N	\N
Harborview-Seahurst-Glenhaven	Everett	WA	\N	\N
Riverside Park	Fort Lauderdale	FL	950	995
Sierra Springs	San Antonio	TX	\N	1250
Forest Trails	Jacksonville	FL	1195	1195
Trilogy	Corona	CA	\N	1995
Harrison East-South	Tucson	AZ	\N	\N
Rock Island	Fort Lauderdale	FL	\N	1600
Weinland Park	Columbus	OH	\N	799
Wrigleyville	Chicago	IL	1673	1600
Duval	Jacksonville	FL	\N	1050
University South	Palo Alto	CA	\N	\N
Upper Fells Point	Baltimore	MD	1350	1699
Cedar Hills Estate	Jacksonville	FL	795	950
Sunset	Fort Lauderdale	FL	\N	1500
Victory Hills	Albuquerque	NM	\N	600
Newfield	Stamford	CT	\N	\N
Biscayne	Jacksonville	FL	975	\N
Coronado Hills	Austin	TX	655	\N
Richmond Valley	New York	NY	\N	\N
Cathedral Heights	Washington	DC	2246	1985
Beatties Ford-Trinity	Charlotte	NC	890	\N
South Pointe	San Bernardino	CA	\N	1595
Fairwood and Robandee	Kansas City	MO	\N	850
Duclay Forest	Jacksonville	FL	975	999
Arrowhead Farms	San Bernardino	CA	\N	\N
Jacksonville Heights South	Jacksonville	FL	\N	1195
Government Hill Alliance	San Antonio	TX	\N	\N
Sherwood Forest	Charlotte	NC	795	\N
Limberlost	Tucson	AZ	\N	750
Pipers Meadow	San Antonio	TX	\N	\N
Riverview	Seattle	WA	\N	1395
Kirkman South	Orlando	FL	800	1000
Central Business District - Downtown	Kansas City	MO	995	1100
Village 12	Sacramento	CA	\N	1550
West University	Tucson	AZ	1000	700
Virginia Ave	Lexington	KY	\N	900
Lewelling	Milwaukie	OR	\N	\N
Southern Orchards	Columbus	OH	\N	550
Upper East Side	Milwaukee	WI	\N	\N
Quail Hollow	Charlotte	NC	\N	950
Emerald Estates	Bakersfield	CA	\N	1550
Curtis Bay	Baltimore	MD	800	1000
University	San Bernardino	CA	\N	\N
Eastmont Hills	Oakland	CA	\N	2200
Arlington Park	Sarasota	FL	\N	\N
Downtown	Salt Lake City	UT	915	1075
Ida B. Wells - Darrow Homes	Chicago	IL	\N	\N
Hogan's Creek	Jacksonville	FL	850	\N
Oakdale South	Charlotte	NC	\N	1000
South Wedge	Rochester	NY	\N	\N
Edgemoor	Saint Petersburg	FL	\N	\N
South Kilbourne	Columbia	SC	795	575
Hilliard Green	Columbus	OH	\N	\N
NE - Sterling	San Bernardino	CA	\N	1300
Mahncke Park	San Antonio	TX	\N	650
Willow Creek	Kansas City	MO	665	699
Ivy Hill	Oakland	CA	\N	\N
Moorings	Naples	FL	2500	5000
Great Neck Estates	Great Neck	NY	\N	4500
Westchester	Charlotte	NC	795	825
West Gate	Austin	TX	\N	1100
Hedrick Acres	Tucson	AZ	595	695
North Star	Anchorage	AK	\N	1150
Pendleton Heights	Kansas City	MO	\N	\N
Hudson	San Bernardino	CA	\N	\N
Centennial Park	Santa Ana	CA	\N	\N
Colonial Village	Sacramento	CA	\N	\N
Park Circle	Baltimore	MD	\N	\N
Oakdale	Portland	ME	\N	1100
East Community Team North	Kansas City	MO	\N	\N
Olde Whitehall	Charlotte	NC	\N	1100
Thousand Oaks	San Antonio	TX	729	\N
Broadleigh	Columbus	OH	\N	\N
Sylvan Park	Nashville	TN	\N	\N
Aviation Sub.	Detroit	MI	\N	800
Old Town-Chinatown	Portland	OR	1200	\N
Penrose-Fayette Street Outreach	Baltimore	MD	\N	1150
Sullivan's Gulch	Portland	OR	\N	995
Naples	Long Beach	CA	\N	2400
Chinatown	Chicago	IL	\N	\N
Lake Forest	Jacksonville	FL	\N	800
Thornhill	Mobile	AL	870	\N
Seven Eagles	Charlotte	NC	\N	\N
Galindo	Austin	TX	940	1350
Finley Farms	Gilbert	AZ	\N	\N
Eliot	Portland	OR	\N	1195
Cherrydale	Arlington	VA	\N	\N
City Center	Toledo	OH	\N	\N
Eastmont	Oakland	CA	\N	1200
Island Estate Civic Association	Clearwater	FL	1500	2300
Lake Hollingsworth	Lakeland	FL	\N	\N
Parkside	Portland	ME	850	830
South University	Eugene	OR	\N	\N
Rain Tree	Charlotte	NC	770	\N
Castlemont	Oakland	CA	\N	\N
East Foothills	Boulder	CO	\N	1655
Woodbine	Sacramento	CA	\N	\N
Muscupiabe	San Bernardino	CA	\N	\N
Lincoln Villas	Jacksonville	FL	\N	\N
Southpoint	Jacksonville	FL	1090	795
Irish Channel	New Orleans	LA	\N	1850
Eugene Field	Tulsa	OK	\N	\N
Washington Village	Baltimore	MD	1200	1150
Herlong	Jacksonville	FL	\N	1150
Montlake	Seattle	WA	\N	1295
Sunny Slope	San Antonio	TX	\N	\N
Takoma	Washington	DC	\N	1835
Northgate	Seattle	WA	\N	\N
Northwood Hills	West Palm Beach	FL	\N	1150
Frasier Meadows	Boulder	CO	\N	\N
Southgate Triangle	Missoula	MT	\N	775
Snell Isle	Saint Petersburg	FL	1350	\N
Indiana Forest	Columbus	OH	\N	625
Highland Park	Grand Rapids	MI	\N	750
Presidio	San Francisco	CA	3575	2916
Morningside	Pittsburgh	PA	\N	\N
Holden-Parramore	Orlando	FL	\N	\N
Castle Manor	Milwaukee	WI	\N	\N
Plaza-Shamrock	Charlotte	NC	575	750
Willow Park	Aurora	CO	\N	\N
Midlothian	Richmond	VA	\N	\N
East Cesar Chavez	Austin	TX	1179	\N
Judkins Park	Seattle	WA	\N	\N
Wilson	San Bernardino	CA	\N	\N
Downtown Business District	Bellingham	WA	\N	\N
Rosedale Park	Detroit	MI	\N	\N
High Country	San Antonio	TX	\N	\N
Huguenot	Richmond	VA	\N	\N
Courier City	Tampa	FL	1400	1295
Laguna	Santa Barbara	CA	\N	1200
Candler Park	Atlanta	GA	1200	\N
Heritage Hill	Grand Rapids	MI	\N	925
Alderman Park	Jacksonville	FL	\N	\N
Cox	Oakland	CA	\N	\N
Glen Oaks	Baltimore	MD	\N	\N
Bywater	New Orleans	LA	\N	\N
Parkwood Maintenance	San Antonio	TX	\N	\N
Mount Vernon	San Bernardino	CA	\N	\N
Pittsburgh	Atlanta	GA	\N	825
Eastern 49-63	Kansas City	MO	\N	\N
Concordia	Milwaukee	WI	\N	\N
A Mountain	Tucson	AZ	\N	\N
Arrowview	San Bernardino	CA	\N	\N
Collingwood	Charlotte	NC	\N	550
Northwest Harbor	East Hampton	NY	36000	38000
Park Village	San Antonio	TX	\N	\N
Clanton Park-Roseland	Charlotte	NC	\N	\N
West End	Washington	DC	3265	2875
Frick	Oakland	CA	\N	\N
Plaza Midwood	Charlotte	NC	1300	960
Tuscany-Canterbury	Baltimore	MD	1400	\N
Sugaw Creek-Ritch Ave	Charlotte	NC	\N	\N
Kirkman North	Orlando	FL	785	985
Corryville	Cincinnati	OH	\N	\N
Village 2	Sacramento	CA	\N	\N
Governours Square	Columbus	OH	620	\N
Bayou Oaks	Sarasota	FL	\N	950
Swain Oaks	Stockton	CA	\N	650
Allen	Buffalo	NY	\N	750
Oceana	Virginia Beach	VA	750	785
Burleith	Washington	DC	\N	3150
Whites Bend	Nashville	TN	745	\N
South Carthay	Los Angeles	CA	\N	1997
Downtown	Eugene	OR	995	565
Shepherd Park	Washington	DC	\N	\N
Tahoe Park	Sacramento	CA	\N	\N
Noralto	Sacramento	CA	\N	\N
Prairie Hills	Town of Madison	WI	\N	\N
Navy Yard	Washington	DC	2435	2495
King-Lincoln-Bronzeville	Columbus	OH	\N	495
Jefferson	San Antonio	TX	\N	\N
Sobrante Park	Oakland	CA	\N	\N
Yankee Hill	Milwaukee	WI	1650	1350
Lake Country	Fort Worth	TX	\N	\N
The Eye	Detroit	MI	\N	800
Parkway	Albuquerque	NM	\N	\N
Southwest	Atlanta	GA	\N	\N
Terrace Village	Pittsburgh	PA	\N	\N
Santa Fe	Oakland	CA	\N	\N
New Dorp Beach	New York	NY	\N	\N
Eastview	Richmond	VA	\N	\N
Hayward Park	San Mateo	CA	\N	\N
Forest Knolls	San Francisco	CA	\N	3070
Avalon Park	Chicago	IL	\N	630
South Campus	Town of Madison	WI	1745	1645
Twin Peaks	San Francisco	CA	\N	2600
Covenant Blu-Grand Center	Saint Louis	MO	950	\N
West End	New Orleans	LA	\N	\N
River Oaks	Fort Lauderdale	FL	1500	1300
Marlborough Heights - Marlborough Pride	Kansas City	MO	\N	650
North Highland	Arlington	VA	1560	1800
Downtown	Boston	MA	2600	3400
Lockeland Springs	Nashville	TN	\N	\N
Meadows Village	Las Vegas	NV	\N	1350
Graceland West	Chicago	IL	1400	1600
Royal Lakes	Jacksonville	FL	800	\N
Greenspring	Baltimore	MD	\N	\N
Eads-Fisherville	Memphis	TN	\N	1175
Canterbury	Mobile	AL	\N	\N
Tri-Taylor	Chicago	IL	1300	1450
McKinley	Albuquerque	NM	\N	\N
Indian Creek	Denver	CO	\N	\N
Conway	Orlando	FL	775	800
Georgian Heights	Columbus	OH	\N	\N
West Albany	Columbus	OH	\N	\N
Sagepointe	Bakersfield	CA	\N	780
Blenman-Elm	Tucson	AZ	\N	875
Coral Ridge Isles	Fort Lauderdale	FL	1350	1250
Downtown North	Palo Alto	CA	\N	\N
South End	Stamford	CT	2980	\N
Bluff Acres	Town of Madison	WI	\N	\N
El Dorado - Oates Prairie	Houston	TX	\N	\N
South Los Altos	Albuquerque	NM	\N	550
Los Prados	San Mateo	CA	\N	\N
Woodbine	Nashville	TN	\N	575
Sunset Road	Charlotte	NC	\N	1050
Fry Springs	Charlottesville	VA	\N	1195
Irvine Health and Science Complex	Irvine	CA	\N	1960
Bluff Park	Long Beach	CA	\N	2450
Brentwood	Washington	DC	\N	\N
Browncroft	Rochester	NY	\N	\N
Camelot 1	San Antonio	TX	\N	\N
Hidden Hills	Jacksonville	FL	\N	\N
Boise	Portland	OR	1195	2025
Friedrich Wilderness Park	San Antonio	TX	\N	1430
Miracle Manor	Tucson	AZ	\N	695
Turtle Ridge	Irvine	CA	2750	3500
Colonialtown North	Orlando	FL	\N	1150
North Park	San Bernardino	CA	\N	\N
Pepperwood	Tempe	AZ	\N	\N
Mechanicsville	Atlanta	GA	1000	995
United Amigos	Mesa	AZ	\N	\N
Amtrak	San Bernardino	CA	\N	\N
Old Naples	Naples	FL	2200	4500
Claremont	Mobile	AL	\N	\N
Wilshire Village	San Antonio	TX	615	928
Upper East	Santa Barbara	CA	\N	\N
Dignowity Hill	San Antonio	TX	\N	925
Brookfield Village	Oakland	CA	\N	\N
Westfield	Baltimore	MD	\N	\N
Eastgate	Bellevue	WA	\N	1700
Uptown	Albuquerque	NM	\N	\N
Wayland	Providence	RI	1600	1100
Leisure World	Mesa	AZ	\N	2400
English Avenue	Atlanta	GA	\N	950
Eight Mile Wyoming	Detroit	MI	\N	700
Downtown	San Antonio	TX	759	1800
Holiday Park	Stockton	CA	\N	850
East Isles	Minneapolis	MN	\N	\N
Lakewood	Saint Petersburg	FL	815	995
West View	Atlanta	GA	\N	775
Mckinley	Minneapolis	MN	\N	\N
Sunnyside	New York	NY	\N	\N
Richmond Heights	Orlando	FL	\N	\N
Historic Kenwood	Saint Petersburg	FL	900	850
Ortega Farms	Jacksonville	FL	\N	825
Sunset Heights	El Paso	TX	\N	\N
Highlandtown	Baltimore	MD	\N	\N
DeBaliviere Place	Saint Louis	MO	825	800
Hillcrest	Dayton	OH	\N	\N
Pineapple Park - Ibis	West Palm Beach	FL	4000	3000
Potomac Yard-Potomac Greens	Alexandria	VA	2085	\N
Mccormick	Wichita	KS	\N	\N
Skyland	Denver	CO	\N	\N
Heartside	Grand Rapids	MI	\N	\N
Westhill	Mobile	AL	\N	\N
Terra Vista	Bakersfield	CA	\N	\N
Lakemont	Augusta	GA	\N	800
Center Hill	Atlanta	GA	\N	875
Keewaydin	Minneapolis	MN	\N	\N
Parker Ridge	West Palm Beach	FL	\N	\N
Longs Creek	San Antonio	TX	\N	\N
Lyon's Gate	Gilbert	AZ	\N	1275
The Traditions	Chandler	AZ	\N	\N
Pen Lucy	Baltimore	MD	\N	\N
Lackawanna	Jacksonville	FL	\N	\N
Alegre Community	Tempe	AZ	650	895
Sheldon-Charter Oak	Hartford	CT	\N	850
Lynn Knoll	Aurora	CO	\N	829
Singing Arrow	Albuquerque	NM	\N	599
Bennington	Vancouver	WA	\N	\N
Randolph	Richmond	VA	867	1400
Coliseum	Oakland	CA	\N	\N
Harrison	Minneapolis	MN	\N	\N
Tarpon River	Fort Lauderdale	FL	2225	1695
Jefferson Heights	San Antonio	TX	\N	\N
North of Grand	Des Moines	IA	\N	\N
Ravenswood Manor	Chicago	IL	\N	\N
City Park	Denver	CO	1347	\N
Lakewide	Oakland	CA	995	\N
Parkwood Ranch	Mesa	AZ	\N	1100
Soulard	Saint Louis	MO	\N	900
Orchard Ridge Community	Town of Madison	WI	\N	\N
Sendera Ranch	Fort Worth	TX	\N	1295
Panama Park	Jacksonville	FL	\N	650
International District	Seattle	WA	\N	1350
Mount Vernon	Columbus	OH	\N	\N
La Playa	San Diego	CA	2500	2750
Sailboat Bend	Fort Lauderdale	FL	1850	1800
Touro	New Orleans	LA	\N	\N
Cleveland	Minneapolis	MN	\N	\N
Park Estates	Long Beach	CA	\N	\N
Jacksonville Heights West	Jacksonville	FL	800	1036
Baltimore	Mobile	AL	\N	\N
Lake Meadows	Chicago	IL	806	\N
Highland Park	Aurora	CO	\N	\N
Esther Short	Vancouver	WA	720	\N
Foxboro	Columbus	OH	\N	835
Five Oaks	Dayton	OH	\N	\N
Ribault	Jacksonville	FL	\N	\N
Central Avenue	Albany	NY	\N	\N
Sherman Heights	San Diego	CA	\N	\N
Fishkorn	Detroit	MI	\N	790
Live Oaks Square	Tampa	FL	\N	\N
Duboce Triangle	San Francisco	CA	\N	4900
Cottage Grove	Youngstown	OH	\N	\N
Capital View-Stiff	Little Rock	AR	\N	650
Lower Clinton Hill	Newark	NJ	\N	\N
East Baltimore Midway	Baltimore	MD	\N	1050
Bloomfield	New York	NY	\N	\N
Enderly Park	Charlotte	NC	495	675
The Hills of Park North	San Antonio	TX	\N	\N
Medical Center Area	Houston	TX	1468	1650
Marigny	New Orleans	LA	\N	1400
Colonial Manor	Sacramento	CA	\N	\N
Pleasant Plains	New York	NY	\N	1200
Navco	Mobile	AL	\N	700
Winston Park	Saint Petersburg	FL	\N	\N
Adamsville	Atlanta	GA	\N	\N
Wakefield	Washington	DC	1646	1560
RP Sports Complex	Sacramento	CA	\N	\N
Spring Creek Neighborhood Alliance	San Antonio	TX	\N	\N
Wendover-Sedgewood	Charlotte	NC	1020	1250
San Marco	Jacksonville	FL	750	675
Factoria	Bellevue	WA	1475	2000
Central Park	New York	NY	2850	3695
Fairlawn	Washington	DC	\N	\N
Lake Forest Hills	Jacksonville	FL	\N	1000
North Town Fork Creek	Kansas City	MO	\N	\N
The Palisades	Washington	DC	\N	2195
New Scotland	Albany	NY	\N	\N
Stockdale West	Bakersfield	CA	\N	\N
Park East	Sarasota	FL	825	950
Durrs Homeowners	Fort Lauderdale	FL	\N	995
Harriet Creek Ranch	Fort Worth	TX	\N	1300
SBIC	Baltimore	MD	\N	1900
Clearwater Beach Association	Clearwater	FL	2000	3000
Southwest Quadrant	Alexandria	VA	2155	2166
Truxton Circle	Washington	DC	\N	2500
Terrell Heights	San Antonio	TX	949	1045
Downtown	Sarasota	FL	2200	3200
Wilshire	San Antonio	TX	\N	\N
Waverly Hills	Arlington	VA	\N	\N
Natomas Crossing	Sacramento	CA	\N	1350
North Campus	Columbus	OH	\N	590
Lakewood Heights	Atlanta	GA	800	\N
Lewis and Clark	Missoula	MT	\N	650
Forest Park West	Columbus	OH	\N	\N
Cedar-Isles-Dean	Minneapolis	MN	1970	2279
Sunset	Tempe	AZ	625	795
Breezy Point	New York	NY	\N	3005
Carver	Mobile	AL	\N	\N
Dayton-Weequahic Park	Newark	NJ	\N	\N
Downtown	Olympia	WA	\N	\N
Mckinney	Austin	TX	900	\N
Twin Towers	Dayton	OH	\N	\N
Northridge Estates	Dayton	OH	\N	\N
Madison Area	Grand Rapids	MI	\N	795
South Rose Hill	Kirkland	WA	\N	\N
Northside	Missoula	MT	\N	\N
Lockhill Estates	San Antonio	TX	\N	\N
Riverview	Tulsa	OK	\N	\N
Moncrief Park	Jacksonville	FL	\N	\N
Bridle Trails	Kirkland	WA	\N	\N
Amaryllis Park	Sarasota	FL	\N	\N
Cathedral Park	Portland	OR	\N	\N
University City North	Charlotte	NC	819	\N
Downtown	Portland	ME	1600	1525
Central Northside	Pittsburgh	PA	\N	\N
St. Catherine's Gardens	Kansas City	MO	\N	\N
Galloway Ridge	Columbus	OH	\N	\N
Reynoldstown	Atlanta	GA	1200	900
Sedgefield	Charlotte	NC	895	995
The Bush	Chicago	IL	\N	\N
Better Waverly	Baltimore	MD	\N	\N
South Green	Hartford	CT	\N	795
Shelby Park	Louisville	KY	\N	650
Central City-Liberty Wells	Salt Lake City	UT	\N	\N
Woodlawn	Mobile	AL	\N	750
Canterbury Green	Fort Wayne	IN	649	584
Sunset Cliffs	San Diego	CA	\N	\N
Greenwich Hills	Mobile	AL	\N	\N
West Congress	Austin	TX	1250	1025
Golf Course Terrace	Sacramento	CA	\N	1150
Boulevard Bluffs	Everett	WA	\N	1320
West Portal	San Francisco	CA	\N	\N
Ashbrook-Clawson Village	Charlotte	NC	995	1000
Garfield Heights	Washington	DC	\N	1150
Tiger Hole-Secret Woods	Jacksonville	FL	\N	\N
Carthage	Cincinnati	OH	\N	\N
Guide Meridian	Bellingham	WA	\N	\N
Richland Park	Richardson	TX	\N	\N
Dobson Woods	Mesa	AZ	\N	\N
First Ward	Charlotte	NC	1000	1280
Douglas	Washington	DC	\N	\N
Pearl-Meigs-Monroe	Rochester	NY	595	\N
Sheridan	Minneapolis	MN	\N	\N
The Gate District	Saint Louis	MO	\N	850
Meyer Park	Tempe	AZ	776	1195
Boulevard Park	Sacramento	CA	\N	725
Hamilton	Fort Wayne	IN	\N	\N
Fairway Bend	Fort Worth	TX	\N	919
Dennis Port	Dennis	MA	\N	1100
Slater Rd-Hamilton Circle	Charlotte	NC	\N	\N
Lafayette Square	Saint Louis	MO	\N	\N
McClymonds	Oakland	CA	\N	\N
Hope	Providence	RI	\N	1050
Olde Towne	Toledo	OH	\N	\N
The Strip	Las Vegas	NV	1600	2000
Oakbrook	Vancouver	WA	\N	\N
Palm Beach Lakes	West Palm Beach	FL	\N	1500
Perkerson	Atlanta	GA	\N	\N
Dodge Flower	Tucson	AZ	\N	580
Mission Valley West	San Diego	CA	1700	1650
Marrion	Vancouver	WA	\N	\N
Gardenland	Sacramento	CA	\N	\N
Barrio Hollywood	Tucson	AZ	\N	\N
Riverside Heights	Tampa	FL	\N	\N
Walnut Hills	Columbus	OH	\N	\N
North Rosslyn	Arlington	VA	2800	2495
Fairways Forest	Jacksonville	FL	\N	\N
University Park Estates	Long Beach	CA	\N	\N
Greektown	Baltimore	MD	\N	\N
North Highland Park	Richmond	VA	\N	850
Strawberry Manor	Sacramento	CA	\N	\N
West De Paul	Chicago	IL	1725	2700
East Lake	Atlanta	GA	\N	\N
Crown Hill	Seattle	WA	\N	\N
Mohican Regent	Detroit	MI	\N	\N
Center Square	Albany	NY	\N	800
Tampa International Airport Area	Tampa	FL	1100	1235
Holiday Park	Albuquerque	NM	\N	\N
Lake Ridge	Fort Lauderdale	FL	1850	1600
Alta Vista	San Antonio	TX	\N	\N
Lauriedale	San Mateo	CA	1740	\N
Latah Valley	Spokane	WA	\N	1400
West Bayside	Portland	ME	\N	\N
Rio Vista	Fort Lauderdale	FL	1950	2400
Monterey	Orlando	FL	\N	\N
Orlando International Airport	Orlando	FL	\N	\N
Saint Joseph	Louisville	KY	\N	\N
Southwood	Jacksonville	FL	\N	\N
River Bend	Des Moines	IA	\N	\N
Ruskin Hills	Kansas City	MO	\N	850
Denny Triangle	Seattle	WA	1575	2450
Kearny Mesa	San Diego	CA	\N	1967
Palmetto Beach	Tampa	FL	\N	\N
Interbay	Tampa	FL	\N	1400
Mark Twain	Richardson	TX	\N	\N
Summerhill	Atlanta	GA	\N	\N
Cody	Mobile	AL	\N	725
Buena Vista Park	San Francisco	CA	\N	3600
Locust Point Industrial Area	Baltimore	MD	\N	1900
North Charlotte	Charlotte	NC	890	1200
Burr Oaks	Town of Madison	WI	\N	725
Coppin Heights - Ash-Co-East	Baltimore	MD	\N	1060
Hermitage Hills	Nashville	TN	\N	585
Shockoe Bottom	Richmond	VA	1025	1082
Clifton	Louisville	KY	\N	\N
Slate Hill	Columbus	OH	\N	895
Thomasville Heights	Atlanta	GA	\N	695
Orchard Hills	Irvine	CA	\N	2100
Euclid Heights	Saint Petersburg	FL	\N	\N
Sterling	Charlotte	NC	725	\N
St. Louis Place	Saint Louis	MO	\N	\N
Downtown Des Moines	Des Moines	IA	725	1185
Smoketown Jackson	Louisville	KY	\N	\N
Downtown Charlotte	Charlotte	NC	1175	1400
Falcon Ridge	Fort Worth	TX	\N	1250
Brookside Woods	Columbus	OH	\N	900
Fossil Park	Fort Worth	TX	\N	\N
Gateway	Saint Petersburg	FL	\N	\N
DUMBO	New York	NY	3600	3850
Llanfair	Mobile	AL	\N	\N
Sunset	Boise	ID	\N	\N
Louis Park	Stockton	CA	\N	\N
Newton Booth	Sacramento	CA	\N	750
Patch	Saint Louis	MO	\N	680
Middle East	Baltimore	MD	1300	1300
Poinsettia Heights	Fort Lauderdale	FL	1850	1595
Five Points	Detroit	MI	\N	\N
Riss Lake	Kansas City	MO	\N	\N
Brightwood Park	Washington	DC	\N	1375
Dinsmore	Jacksonville	FL	\N	\N
Twinbrooks	Saint Petersburg	FL	\N	875
Carino Estates	Chandler	AZ	\N	\N
Brookhaven	Atlanta	GA	\N	\N
East Central	Fort Wayne	IN	725	\N
Grier Heights	Charlotte	NC	450	650
Peachtree Hills	Atlanta	GA	825	\N
Central Business District	San Mateo	CA	\N	3401
Biscayne Terrace	Jacksonville	FL	\N	1100
East Riverside	New Orleans	LA	\N	\N
Poncey-Highland	Atlanta	GA	\N	\N
Twelve Oaks	Chandler	AZ	\N	1295
Southeast Quality	South Bend	IN	\N	575
Mordecai	Raleigh	NC	\N	1250
Madison Park	Baltimore	MD	1166	1050
Russell Woods	Detroit	MI	\N	650
Poppleton	Baltimore	MD	\N	\N
Hyatt Park	Columbia	SC	\N	\N
Forest Park Southeast	Saint Louis	MO	\N	925
West Markham	Little Rock	AR	\N	\N
Clifton Heights	Saint Louis	MO	\N	750
Oak Grove Estates	San Antonio	TX	\N	\N
Lake Watkins	Lakeland	FL	\N	\N
Carver	Washington	DC	\N	\N
Red Ridge South	Kansas City	MO	689	\N
Franklin Park	Columbus	OH	\N	550
Federal Hill	Baltimore	MD	2100	1700
Fox Park	Saint Louis	MO	\N	700
Oak Park Northwest	Kansas City	MO	\N	650
Prospect Park South	New York	NY	1600	1350
Emma Dickinson Orchard Homes	Missoula	MT	\N	\N
Monroe Ward	Richmond	VA	765	\N
NTNA - College	Tempe	AZ	801	748
Marine Villa	Saint Louis	MO	\N	\N
Langdon	Washington	DC	\N	\N
Lake Somerset	Lakeland	FL	\N	\N
Starmount	Charlotte	NC	\N	1450
Fairmount Park	San Diego	CA	\N	\N
Upper Lawrenceville	Pittsburgh	PA	\N	\N
S Y Jackson	Albuquerque	NM	\N	\N
Franklin Square	Baltimore	MD	\N	\N
Ortega	Jacksonville	FL	\N	\N
Guilford Center	Guilford	CT	\N	\N
Rolling Hills Ranch	Chula Vista	CA	\N	\N
Midway	Henderson	NV	\N	1250
Northern Hills	San Antonio	TX	\N	\N
Westover	Stamford	CT	\N	\N
La Gorce	Miami Beach	FL	\N	6900
Pheasant Hill	Dayton	OH	\N	\N
Colonial Village	Arlington	VA	2049	1990
Paces	Atlanta	GA	\N	1420
Downtown CBD	Little Rock	AR	\N	1090
Encanto	Mesa	AZ	\N	\N
Houghton	Tucson	AZ	\N	\N
Ventura	Palo Alto	CA	\N	\N
Washington Square	Mobile	AL	\N	\N
Knight Park - Howell Station	Atlanta	GA	\N	\N
Holly Hills	Saint Louis	MO	\N	675
Riverfront	Missoula	MT	\N	\N
North Waterfront	San Francisco	CA	\N	3475
Inner Harbor	Baltimore	MD	1898	\N
Waverly	Baltimore	MD	\N	1200
North Kenwood	Saint Petersburg	FL	\N	\N
Old Fort Lowell	Tucson	AZ	\N	\N
Peoplestown	Atlanta	GA	\N	900
Summit Park	Albuquerque	NM	\N	\N
West Oakland	Pittsburgh	PA	1297	\N
Second Creek	Mobile	AL	835	\N
Piney Knolls	Richmond	VA	\N	\N
Magnolia	Stockton	CA	\N	550
Rosedale	Denver	CO	\N	\N
Belmont	Charlotte	NC	\N	595
White Bridge	Nashville	TN	\N	\N
West Mesa	Santa Barbara	CA	\N	1995
Maplewood	Portland	OR	\N	\N
Las Palmas	Oakland	CA	\N	\N
Cedmont	Baltimore	MD	\N	960
Euclid-St Pauls	Saint Petersburg	FL	\N	\N
Thomaston	Great Neck	NY	2150	2285
Bellemeade	Richmond	VA	750	\N
South River Gardens	Atlanta	GA	\N	913
Buckhorn	Mesa	AZ	\N	895
Feldman's	Tucson	AZ	\N	775
South Plaza	Kansas City	MO	1065	\N
Skies West	Albuquerque	NM	\N	1075
Council Oak	South Bend	IN	\N	\N
Lake Road	Milwaukie	OR	\N	\N
Shingle Creek	Minneapolis	MN	\N	\N
Rosemont	Baltimore	MD	\N	1000
Dawson	Austin	TX	1511	1343
Tempe Royal Estates	Tempe	AZ	\N	\N
Fondren Gardens	Houston	TX	\N	\N
Livingston - McNaughten	Columbus	OH	\N	\N
Algeirs Point	New Orleans	LA	\N	\N
Jefferson Park	Denver	CO	\N	\N
Palm Club Village	West Palm Beach	FL	850	1150
Grandmont No.1	Detroit	MI	\N	950
Flagler Heights	Fort Lauderdale	FL	1850	1800
Cascade Avenue-Road	Atlanta	GA	\N	825
Preserve South	Columbus	OH	\N	\N
Monterey	Jacksonville	FL	725	750
Carver	Richmond	VA	1020	1200
Airport	Sacramento	CA	\N	\N
Croissant Park	Fort Lauderdale	FL	2200	1750
Highland	Albuquerque	NM	\N	595
Vista del Norte	Albuquerque	NM	\N	\N
Wilder Park	Louisville	KY	\N	\N
Normandy Village	Jacksonville	FL	\N	995
Westover	Richmond	VA	600	\N
Greenbush	Town of Madison	WI	\N	1275
Kellogg School	Wichita	KS	\N	599
Trouville	Columbus	OH	\N	\N
Mapleton Hill	Boulder	CO	\N	1900
Ridgemoor	Grand Rapids	MI	\N	\N
Brookwood	Mobile	AL	\N	\N
Sand Key Civic Association	Clearwater	FL	2200	2500
Natomas Creek	Sacramento	CA	\N	\N
Oak Creek	San Antonio	TX	\N	1150
RMMA	Austin	TX	1555	\N
Northern Barton Heights	Richmond	VA	\N	875
Lake Maggiore	Saint Petersburg	FL	\N	\N
Woodmere	Baltimore	MD	\N	\N
Sweet Auburn	Atlanta	GA	972	1221
Ashley Park	Charlotte	NC	600	725
Edgewood	Fort Lauderdale	FL	1340	1650
Oak Flower	Tucson	AZ	\N	\N
Hidden Valley	Bellevue	WA	1540	1795
Elliott	Pittsburgh	PA	\N	\N
Vasa	Bellevue	WA	\N	\N
Hillside	Portland	OR	\N	1450
Eastwood	Nashville	TN	\N	\N
Dixieland	Lakeland	FL	\N	\N
Bartlett Park	Saint Petersburg	FL	\N	800
East Calhoun	Minneapolis	MN	\N	\N
Harbordale	Fort Lauderdale	FL	1600	1565
Hanover Place	Kansas City	MO	550	750
Moorpark	Glendale	CA	\N	\N
South Forest Park	Everett	WA	\N	\N
Corn Hill	Rochester	NY	\N	\N
Greenwich Village	Dayton	OH	\N	\N
Rincon Heights	Tucson	AZ	\N	850
Skyland	Washington	DC	\N	\N
South Lake Union	Seattle	WA	\N	1930
Duquesne Heights	Pittsburgh	PA	\N	\N
Fifth City	Chicago	IL	\N	975
Kalorama	Washington	DC	\N	2500
Bay Creek	Town of Madison	WI	\N	\N
Bolton	Atlanta	GA	\N	\N
Claremont	Arlington	VA	\N	\N
Bridgeview - Greenlawn	Baltimore	MD	\N	\N
Browns Mill Park	Atlanta	GA	\N	\N
Fiesta Park Village	Mesa	AZ	\N	\N
Buckhead Forest	Atlanta	GA	1365	1455
Hanlon-Longwood	Baltimore	MD	\N	\N
Tuxedo	Oakland	CA	\N	\N
East Bayside-India Street	Portland	ME	\N	\N
Belmont	Detroit	MI	\N	750
Briarwood	Little Rock	AR	\N	\N
Jefferson Park	Tucson	AZ	\N	1025
Washington Hill	Baltimore	MD	\N	1350
Freedom Park	Charlotte	NC	\N	\N
Benning	Washington	DC	985	\N
Cylburn	Baltimore	MD	\N	\N
Oakhurst	Charlotte	NC	\N	\N
McPherson Ranch	Fort Worth	TX	\N	1450
Mountain Arroyos	El Paso	TX	\N	875
Southwest	West Palm Beach	FL	\N	\N
Arroyo Chico	Tucson	AZ	550	\N
Essex Village	Essex	CT	1200	1100
Ralph Bunche	Oakland	CA	\N	\N
Walbrook	Baltimore	MD	\N	\N
San Pablo Gateway	Oakland	CA	\N	2206
Prairie Shores	Chicago	IL	\N	1035
Hazelwood	Louisville	KY	\N	\N
Madison - Eastend	Baltimore	MD	\N	\N
Baxter	Grand Rapids	MI	\N	750
Citizens on Alert	San Antonio	TX	\N	\N
Royal Ridge	San Antonio	TX	\N	\N
Harrisburg	Augusta	GA	\N	\N
Three Chopt	Richmond	VA	\N	\N
Whiteoak	Charlotte	NC	930	\N
Vine City	Atlanta	GA	\N	\N
Campus Commons	Sacramento	CA	945	\N
Swope Parkway - Elmwood	Kansas City	MO	\N	600
Church Hill	Richmond	VA	850	1050
Navarre	New Orleans	LA	\N	\N
Produce & Waterfront	Oakland	CA	1683	2317
Riviera Bay	Saint Petersburg	FL	\N	1400
Lettered Streets	Bellingham	WA	\N	\N
Tuttle West	Columbus	OH	995	\N
East Augusta	Augusta	GA	\N	\N
Arlington	Baltimore	MD	\N	\N
The Gap	Chicago	IL	\N	\N
Regina	Minneapolis	MN	\N	\N
Riverdale	Little Rock	AR	950	\N
Shroyer Park	Dayton	OH	525	\N
South Lake Morton	Lakeland	FL	\N	\N
Northwood	West Palm Beach	FL	\N	1100
Trilogy	Gilbert	AZ	\N	\N
Mariners Village	Orlando	FL	\N	\N
Central Business District	New Orleans	LA	1740	2300
Curtis	San Bernardino	CA	\N	\N
Hammond Park	Atlanta	GA	\N	\N
Indian Beach-Sapphire Shores	Sarasota	FL	\N	\N
Edgewater Glen	Chicago	IL	780	1400
Troy Hill	Pittsburgh	PA	1385	\N
Fairgrounds	Tucson	AZ	\N	\N
West Hills	Spokane	WA	\N	\N
Las Vistas	Tucson	AZ	\N	\N
Cherry Street	Tulsa	OK	\N	\N
Lake Como	Orlando	FL	\N	\N
Lasalle Area	South Bend	IN	\N	600
Springvale	San Antonio	TX	\N	\N
Ridgewood	Town of Madison	WI	865	\N
Isla Del Sol	Saint Petersburg	FL	2250	2200
Mariners Island	San Mateo	CA	\N	\N
Brookwood Hills	Atlanta	GA	\N	\N
Progresso Village	Fort Lauderdale	FL	\N	1200
Property Owners of Northhampton	San Antonio	TX	\N	1200
Carver City	Tampa	FL	1072	1149
Historic Uptown	Saint Petersburg	FL	\N	675
Cold Sprint Park	Milwaukee	WI	\N	\N
Mt. Paran - Northside	Atlanta	GA	1850	\N
Lincoln Heights	Charlotte	NC	\N	\N
University Hts	Albuquerque	NM	\N	\N
Northview Hills	Tampa	FL	\N	\N
Wentworth Holland	Oakland	CA	\N	\N
Northwest Dallas	Dallas	TX	\N	\N
Diamond Heights	San Francisco	CA	\N	\N
Hunter Hills	Atlanta	GA	\N	900
Church Hill North	Richmond	VA	\N	875
Southside	Jacksonville	FL	1195	1195
St. Cyrils	Tucson	AZ	\N	\N
Hidden Meadow	San Antonio	TX	\N	\N
Touchstone Village-Elm Lane	Charlotte	NC	745	\N
Eucalyptus Hill	Santa Barbara	CA	\N	\N
Bella Vista	Vancouver	WA	\N	\N
Riviera	Mobile	AL	\N	\N
Osuna Park	Albuquerque	NM	\N	\N
Heart of Missoula	Missoula	MT	\N	675
North Dodge	Tucson	AZ	\N	650
Downtown	Boise	ID	1200	\N
Hwy 51-Park Road	Charlotte	NC	\N	\N
Princeton Lakes	Atlanta	GA	\N	1500
Flying Horse	Colorado Springs	CO	\N	\N
Yale-Heights	Baltimore	MD	\N	\N
Cedarhurst	Richmond	VA	\N	\N
Providence Park	Charlotte	NC	\N	\N
Harborview	Jacksonville	FL	\N	\N
Earlewood	Columbia	SC	\N	1100
Highland	Oakland	CA	\N	\N
West Slope	Beaverton	OR	\N	\N
Midtown-Edmondson	Baltimore	MD	\N	\N
Dearborn Park	Chicago	IL	1600	1750
Highlands	Boise	ID	\N	\N
Saint Josephs	Baltimore	MD	\N	\N
West Douglas	Kalamazoo	MI	\N	\N
Mountainbrook	Charlotte	NC	\N	\N
East Aurora	Boulder	CO	\N	1500
Clearbrook Park	Monroe Township	NJ	\N	\N
North University	Tucson	AZ	\N	\N
South Riverside	Jacksonville	FL	\N	\N
Nws Cooperative Alliance	South Bend	IN	\N	550
Paradise Park	Oakland	CA	\N	\N
Swansboro West	Richmond	VA	\N	\N
Maysville	Mobile	AL	\N	\N
Parkland Estates	Tampa	FL	\N	\N
Edgewood Manor	Jacksonville	FL	\N	\N
Sweetwater	Jacksonville	FL	\N	950
York	Bellingham	WA	\N	\N
Jeff Davis	Richmond	VA	590	\N
Hi-Pointe	Saint Louis	MO	\N	775
Fairfax	Oakland	CA	\N	\N
Overland	Denver	CO	1075	1215
North Cleveland Park	Washington	DC	\N	2340
Drexel Park	Tucson	AZ	\N	\N
Empire Point	Jacksonville	FL	990	700
Ridge St	Charlottesville	VA	\N	\N
South East Ravenswood	Chicago	IL	1150	1080
Sunnyland	Bellingham	WA	\N	\N
Spring Glen	Jacksonville	FL	\N	\N
CSU Bakersfield	Bakersfield	CA	\N	1175
Meadow Homes	Vancouver	WA	\N	800
Brewery District (including Whittier Peninsula)	Columbus	OH	\N	1245
College Park	Jacksonville	FL	\N	\N
Melrose	Nashville	TN	\N	\N
Toler Heights	Oakland	CA	\N	\N
Lake Eola Heights	Orlando	FL	\N	1000
Hubbard-Richard	Detroit	MI	\N	\N
Shipley Hill	Baltimore	MD	\N	\N
Oakdale	Grand Rapids	MI	\N	\N
Penn North	Baltimore	MD	\N	\N
Cambridge Heights	Milwaukee	WI	\N	\N
Homestead	Portland	OR	\N	\N
University Park	Tempe	AZ	\N	\N
Westshore	San Mateo	CA	\N	2726
Third Ward	Charlotte	NC	1085	1250
Fuller Park	Chicago	IL	\N	\N
Downtown	Hartford	CT	1350	1350
New Town	Jacksonville	FL	\N	\N
Venetia	Jacksonville	FL	895	850
Rancho Buena	Tucson	AZ	\N	\N
Holly Oaks	Jacksonville	FL	\N	\N
South Crichton	Mobile	AL	\N	\N
Point Breeze North	Pittsburgh	PA	\N	\N
Oak Hills	San Antonio	TX	\N	\N
Towne Meadows	Gilbert	AZ	\N	1350
Lake View	Kirkland	WA	\N	1890
South Garden	Richmond	VA	\N	\N
Franz Park	Saint Louis	MO	\N	\N
NoMa	Washington	DC	\N	2896
Santa Fe Hills	Kansas City	MO	\N	\N
Piedmont Heights	Atlanta	GA	1345	1335
Judiciary Square	Washington	DC	2470	2410
Beacon Hills and Harbour	Jacksonville	FL	\N	\N
Meadows of Candleridge	Fort Worth	TX	\N	\N
Clayton-Tamm	Saint Louis	MO	\N	\N
Burton Evergreen	Vancouver	WA	\N	\N
El G.H.E.K.O.	Tucson	AZ	\N	\N
Rattlesnake	Tampa	FL	\N	\N
Gateway Center	Sacramento	CA	\N	1165
Maple Grove - Franklin	Boise	ID	\N	\N
Bay Meadows	San Mateo	CA	\N	\N
Promontory Pointe-Heights	San Antonio	TX	\N	\N
Northbrook	Fort Worth	TX	\N	\N
Castleberry Hill	Atlanta	GA	\N	1400
Wadeview Park	Orlando	FL	\N	\N
Lea Manor	Kansas City	MO	\N	\N
Central Park	Vancouver	WA	\N	\N
Bon Air	Tampa	FL	1200	939
Lawsona-Fern Creek	Orlando	FL	1000	\N
Kevanna Park	Vancouver	WA	\N	\N
The Dominion	San Antonio	TX	\N	\N
Downtown	Santa Ana	CA	\N	\N
Remington	Baltimore	MD	\N	\N
Prince Tucson	Tucson	AZ	\N	\N
Parklane	Baltimore	MD	\N	\N
Carrol-South Hilton	Baltimore	MD	\N	\N
Firestone-Garden Park	Charlotte	NC	\N	900
Santa Fe	Kansas City	MO	\N	\N
South Eola	Orlando	FL	1980	1700
Civano	Tucson	AZ	\N	1100
Historic Ybor	Tampa	FL	\N	1095
Hannon Park	Mobile	AL	\N	525
O'Hare International Airport	Chicago	IL	\N	\N
Lower Rattlesnake	Missoula	MT	\N	\N
Red Mountain Ranch	Mesa	AZ	\N	1600
Ledroit Park	Washington	DC	\N	\N
Franklintown Road	Baltimore	MD	\N	\N
Michigan Oaks	Grand Rapids	MI	\N	\N
North Meadows	Milwaukee	WI	\N	\N
Bonne Hills	Kansas City	MO	\N	\N
Evergreen Park	Palo Alto	CA	\N	\N
Capitol View	Atlanta	GA	\N	\N
Lake Walker	Baltimore	MD	\N	\N
Cortez Hill	San Diego	CA	1695	2150
Mission Hills	Fremont	CA	\N	\N
Hollow Hills	Fort Worth	TX	\N	\N
St Anthony East	Minneapolis	MN	\N	\N
Near Westside Neighborhood	South Bend	IN	\N	\N
Baltimore Highlands	Baltimore	MD	\N	1100
Lloyd	Portland	OR	\N	1107
Tahoe Park South	Sacramento	CA	\N	899
Timberleaf	Orlando	FL	\N	\N
Reisterstown Station	Baltimore	MD	\N	\N
Libbytown	Portland	ME	\N	\N
Chaparral Estates	Gilbert	AZ	\N	\N
Fox Canyon	San Diego	CA	\N	\N
Nuestro	Mesa	AZ	\N	\N
Colonial Heights	Sacramento	CA	\N	\N
German Village Commission	Columbus	OH	995	\N
Mountain Island	Charlotte	NC	\N	1200
Five Mile-Prairie	Spokane	WA	\N	\N
Southeast	Nashville	TN	\N	\N
Fondern-Cherokee Heights	Jackson	MS	\N	\N
Swanston Estates	Sacramento	CA	\N	\N
Audubon Park	Orlando	FL	\N	\N
Sherman Hill	Des Moines	IA	1015	\N
West Downtown	Boise	ID	\N	\N
Dolfield	Baltimore	MD	\N	\N
Cross Creek	Atlanta	GA	1000	1200
Castle Rouge	Detroit	MI	\N	790
C.A.N.D.O.	Mesa	AZ	\N	\N
San Antonio Creekside	San Antonio	TX	\N	\N
Fox Crossing	Chandler	AZ	\N	\N
Webster Park North	Lakeland	FL	\N	\N
Azalea Homes	Saint Petersburg	FL	\N	775
Riverland Village	Fort Lauderdale	FL	\N	1650
East Terrell Hills	San Antonio	TX	\N	\N
Fuller Avenue	Grand Rapids	MI	\N	\N
Channel District	Tampa	FL	1595	1830
Northeast	Tampa	FL	\N	995
West Main Hill	Kalamazoo	MI	\N	1750
Lake Las Vegas	Henderson	NV	1800	1675
Oxbow	San Antonio	TX	\N	875
Farviews & Pattee Canyon	Missoula	MT	\N	\N
Gilbert Ranch	Gilbert	AZ	\N	\N
Highland Farms	San Antonio	TX	\N	\N
Fairburn Mays	Atlanta	GA	\N	\N
Fifeville	Charlottesville	VA	\N	775
Linden Hills and Indian Heights	Kansas City	MO	\N	\N
Printers Row	Chicago	IL	1486	1695
Downtown	West Palm Beach	FL	1250	2200
New Southwest - Mount Clare	Baltimore	MD	\N	950
West Bluff	Albuquerque	NM	\N	\N
Westwood Park	San Francisco	CA	\N	\N
Bankhead	Atlanta	GA	\N	\N
Alcova Heights	Arlington	VA	\N	\N
Peter Howell	Tucson	AZ	\N	\N
Western Skies	Gilbert	AZ	\N	1125
Butcher's Hill	Baltimore	MD	\N	1400
Colonial Town Center	Orlando	FL	\N	\N
Hillcrest	San Antonio	TX	535	\N
Oak Park Southwest	Kansas City	MO	\N	\N
Lavaca	San Antonio	TX	\N	\N
Silver Hill	Albuquerque	NM	\N	700
North State	Santa Barbara	CA	\N	\N
Barclay	Baltimore	MD	\N	1100
Strawberry Hill	Cambridge	MA	\N	2275
South Hyde Park	Kansas City	MO	\N	\N
Melrose	Albany	NY	\N	\N
Brewer's Hill	Milwaukee	WI	1496	\N
Chinquapin Park-Belvedere	Baltimore	MD	\N	\N
Sunbird	Chandler	AZ	\N	\N
Riverfront	Philadelphia	PA	1500	1925
St. Nicholas	Jacksonville	FL	\N	\N
Mark Twain	Albuquerque	NM	\N	\N
Port Morris	New York	NY	\N	1800
Mingo Valley	Tulsa	OK	\N	\N
Stanford Estates	Kansas City	MO	\N	800
Signal Hill	Orlando	FL	\N	825
Harland Terrace	Atlanta	GA	\N	\N
Lake Underhill	Orlando	FL	\N	\N
Swansboro	Richmond	VA	\N	\N
Lakewood - Balmoral	Chicago	IL	790	\N
Jackson Park Highlands	Chicago	IL	\N	735
Mountain Ranch	Mesa	AZ	\N	\N
Carytown	Richmond	VA	\N	925
Longfellow	Kansas City	MO	660	\N
Central Cocoanut	Sarasota	FL	2400	\N
Knoll Ridge	Fort Lauderdale	FL	1150	1095
Weatherby	Detroit	MI	\N	\N
CBD	Kalamazoo	MI	\N	\N
Silver Lake	New York	NY	\N	\N
Friends of Karl Wyler	El Paso	TX	\N	\N
Cabrini	Tucson	AZ	\N	595
McFerrin Park	Nashville	TN	\N	\N
Ridgedale Park	Atlanta	GA	\N	\N
New Era Park	Sacramento	CA	\N	750
Westcliff	Fort Worth	TX	\N	2400
Clam Bayou	Saint Petersburg	FL	\N	\N
North Fairmount	Cincinnati	OH	\N	\N
Lake Aire Palm View	Fort Lauderdale	FL	\N	\N
Cascade	Seattle	WA	1300	1785
Oaks	Garland	TX	\N	\N
Avalon	Bakersfield	CA	\N	\N
Rosemont East	Baltimore	MD	\N	\N
Adams Park	Atlanta	GA	\N	\N
College Place	Columbia	SC	\N	\N
Westside North	Kansas City	MO	\N	\N
Pulaski Industrial Area	Baltimore	MD	\N	\N
Brookhollow	Columbus	OH	\N	\N
North Bellevue	Bellevue	WA	\N	1700
North East	Charlottesville	VA	\N	\N
Granville Station	Milwaukee	WI	\N	\N
Dunn's Marsh	Town of Madison	WI	\N	\N
Loma Vista	Kansas City	MO	\N	\N
Highland Oaks	Saint Petersburg	FL	\N	\N
Central College	Columbus	OH	935	\N
Central Business District	Buffalo	NY	\N	\N
Little Italy	San Diego	CA	1800	2500
Hollins Market	Baltimore	MD	\N	1100
Melrose Mercy - Pine Acres	Saint Petersburg	FL	\N	\N
Callaway-Garrison	Baltimore	MD	\N	\N
Vista Meadows	Fort Worth	TX	\N	\N
Fairfax	Jacksonville	FL	\N	\N
The Ville	Saint Louis	MO	\N	\N
Wendell Phillips	Kansas City	MO	\N	\N
Morris Hill	Boise	ID	\N	\N
El Chaparral Fertile Valley	San Antonio	TX	\N	\N
Landings	Fort Lauderdale	FL	\N	1900
Mill Hill	Baltimore	MD	\N	\N
Biltmore	Jacksonville	FL	\N	\N
Friendship	Pittsburgh	PA	\N	\N
Warrenton-Harmitage Hills-Pinehurst	Lexington	KY	\N	\N
Gay Street	Baltimore	MD	\N	\N
Johnson Village	Charlottesville	VA	\N	\N
Pinewood	West Palm Beach	FL	1000	1295
Atlantic Station	Atlanta	GA	1701	2450
Oak Meadow	San Antonio	TX	\N	\N
Neshota	Mobile	AL	\N	\N
San Mateo	Jacksonville	FL	\N	\N
Washington Heights	Charlotte	NC	\N	\N
Norble and Gregory Ridge	Kansas City	MO	\N	\N
Spectrum	Irvine	CA	\N	1790
Lenox	Atlanta	GA	1806	\N
Hickman Mills South	Kansas City	MO	\N	875
Old Saybrook Center	Old Saybrook	CT	\N	\N
Holdeman	Tempe	AZ	795	\N
Chestnut	Austin	TX	1200	\N
Columbia-Tusculum	Cincinnati	OH	810	\N
Belle Isle	Miami Beach	FL	\N	3100
Allendale	Jacksonville	FL	\N	\N
Redevelopment Area	Naples	FL	\N	\N
Elmhurst Park	Oakland	CA	\N	\N
Jamestown	Lexington	KY	\N	\N
Green Acres	Palo Alto	CA	\N	3255
Windmills West	Chandler	AZ	\N	\N
Malba	New York	NY	\N	\N
Woodland Heights	Richmond	VA	895	\N
Fitchburg	Oakland	CA	\N	\N
Hegenberger	Oakland	CA	\N	\N
Jacksonville University	Jacksonville	FL	\N	\N
Lakeview	Dayton	OH	\N	\N
Greenfield Lakes	Gilbert	AZ	\N	1250
Brownes Addition	Spokane	WA	\N	\N
Alexandra Meadows	Fort Worth	TX	\N	1300
Gililland	Tempe	AZ	\N	\N
Downtown	Dayton	OH	572	\N
Broad Channel	New York	NY	\N	2000
LaSalle Gardens	Detroit	MI	\N	\N
Central Waterfront - Dogpatch	San Francisco	CA	\N	3795
Marshall School	Sacramento	CA	\N	1050
Larsen	Jacksonville	FL	\N	\N
Lockwood Tevis	Oakland	CA	\N	\N
Mosher	Baltimore	MD	\N	\N
Ansley Park	Atlanta	GA	\N	\N
Doolen-Fruitvale	Tucson	AZ	\N	650
Harbor Beach	Fort Lauderdale	FL	\N	4200
Park Plaza East	Tulsa	OK	\N	\N
Blair Park	San Bernardino	CA	\N	850
Harwood	Baltimore	MD	\N	\N
Dixie Hills	Atlanta	GA	\N	\N
Elmhurst	Sacramento	CA	\N	\N
Colonial Park	Columbia	SC	\N	\N
Freret	New Orleans	LA	\N	\N
Middle Hill	Pittsburgh	PA	\N	\N
Roosevelt Estates	West Palm Beach	FL	\N	\N
Highland Park Southern Tip	Richmond	VA	\N	695
Monticello	Fort Worth	TX	\N	1000
North Hyde Park	Kansas City	MO	725	775
Lindsay Ranch	Gilbert	AZ	\N	\N
Howard Park-East Bank	South Bend	IN	\N	\N
Rotary Park	Mesa	AZ	\N	\N
Grove Park	Baltimore	MD	\N	\N
Riverside	Tempe	AZ	659	695
Riveridge	Vancouver	WA	\N	\N
West Riverfront	Tampa	FL	\N	\N
Westerly Hills	Charlotte	NC	\N	800
Country Lane Estates	Kansas City	MO	\N	\N
Cabrini Green	Chicago	IL	\N	\N
Lakewood Terrace	Saint Petersburg	FL	\N	875
Swann Estates	Tampa	FL	\N	\N
Bottineau	Minneapolis	MN	\N	\N
West Calhoun	Minneapolis	MN	1050	1695
Royal Terrace	Jacksonville	FL	\N	\N
Woodland	Oakland	CA	\N	\N
Hills Park	Atlanta	GA	\N	\N
Harlan Heights	Tucson	AZ	\N	\N
Tampa-Bayshore Gardens	Tampa	FL	1300	1275
Upper Shockoe Valley	Richmond	VA	\N	\N
River West	Chicago	IL	1850	2000
Woodridge	San Antonio	TX	\N	\N
Lawrence Park	Sacramento	CA	\N	\N
East Village	San Antonio	TX	\N	\N
Brookland Park	Richmond	VA	\N	\N
Goss Grove	Boulder	CO	2025	1650
Jefferson-Monticello Park	San Antonio	TX	\N	\N
Pine Ridge	Naples	FL	\N	2800
NTNA - Indian Bend	Tempe	AZ	\N	\N
Z'berg Park	Sacramento	CA	\N	\N
Biddle Street	Baltimore	MD	\N	\N
Mozley Park	Atlanta	GA	\N	\N
Southside Park	Sacramento	CA	\N	1095
Woodland Terrace	Tampa	FL	\N	\N
Cascade Heights	Atlanta	GA	\N	\N
Carol Rae Ranch	Gilbert	AZ	\N	\N
Park Village	Gilbert	AZ	\N	\N
Downtown	Santa Barbara	CA	\N	750
Peninsula	Long Beach	CA	\N	\N
Buckhead Village	Atlanta	GA	950	\N
College HIlls	Glendale	CA	\N	\N
Rosemont West	Tucson	AZ	\N	\N
Woodland Park	Columbus	OH	\N	435
East Side Commercial Area	Tampa	FL	\N	\N
South Old Irving Park	Chicago	IL	\N	\N
Madera Parc	Gilbert	AZ	\N	\N
Dixie Belle	Orlando	FL	\N	950
North Tamarind	West Palm Beach	FL	\N	1200
Don Scott	Columbus	OH	\N	\N
Santa Clara	Dayton	OH	\N	\N
Old Town North	Alexandria	VA	\N	2100
Crestline Area	Fort Worth	TX	\N	\N
River Gardens	Sacramento	CA	\N	\N
Fisher	Mobile	AL	\N	\N
Oakwood Gardens	Saint Petersburg	FL	\N	\N
Wood Park	Tempe	AZ	\N	\N
Eastlake Vistas	Chula Vista	CA	\N	2100
Willow Creek	Fort Worth	TX	\N	\N
Amazon	Eugene	OR	\N	\N
Poinciana Park	Fort Lauderdale	FL	1485	985
Hunterwood	Houston	TX	\N	\N
Gladstone Park	Chicago	IL	\N	\N
Dennison Place	Columbus	OH	\N	850
Belvedere	Columbia	SC	\N	\N
South Atlanta	Atlanta	GA	\N	\N
Central Hyde Park	Kansas City	MO	\N	825
Lago Estancia	Gilbert	AZ	\N	\N
Northwest Community Action	Baltimore	MD	\N	\N
McLean Gardens	Washington	DC	2150	2220
Key Coalition	Kansas City	MO	\N	\N
Four by Four	Baltimore	MD	\N	\N
Berkeley Place	Fort Worth	TX	\N	\N
Progressive North West	West Palm Beach	FL	\N	950
Kiwanis Park	Tempe	AZ	\N	\N
Bermuda Riviera	Fort Lauderdale	FL	\N	2700
Royal Harbor	Naples	FL	2100	3000
San Marcos Country Club	Chandler	AZ	\N	1079
Alta Monte	Albuquerque	NM	\N	\N
Monkbridge Gardens	Albuquerque	NM	\N	\N
Civic Center	Denver	CO	1745	2699
Oak Park Southeast	Kansas City	MO	\N	\N
South Commons	Chicago	IL	1050	1250
Villages of Eastridge	Mesa	AZ	\N	1150
Harborview	San Diego	CA	\N	2675
Springfield Lakes	Chandler	AZ	\N	\N
Villa Heights	Charlotte	NC	\N	1000
Chimborazo	Richmond	VA	\N	1050
Stablewood-Valley Hi North	San Antonio	TX	\N	\N
Piccadilly Square	Nashville	TN	\N	\N
Marietta Street Artery	Atlanta	GA	\N	1240
Wilmore	Charlotte	NC	\N	860
Clifton	Jacksonville	FL	\N	\N
East Ybor	Tampa	FL	\N	\N
Wooster Square	New Haven	CT	\N	1250
Almond Park	Atlanta	GA	\N	\N
Main-Starr Hill	Charlottesville	VA	\N	1150
Eastwood Hills West	Kansas City	MO	\N	\N
Westport	Baltimore	MD	\N	\N
Hitchcock	Santa Barbara	CA	\N	\N
Kings Forest	Atlanta	GA	\N	\N
Hillen	Baltimore	MD	\N	\N
Optimist Park NE	Tempe	AZ	\N	\N
Castner Heights	El Paso	TX	\N	\N
Wind Drift	Gilbert	AZ	\N	\N
Parker Street	Lakeland	FL	\N	\N
Maximo	Saint Petersburg	FL	\N	1100
Saint Thomas Square	Tulsa	OK	\N	\N
Triangle State	Austin	TX	1344	1595
Mansion Flats	Sacramento	CA	\N	695
Ben Hill	Atlanta	GA	\N	\N
Greenfield Manor	Jacksonville	FL	\N	\N
Sunnyside	Wichita	KS	\N	\N
Winchester	Baltimore	MD	\N	\N
Self Help Neighborhood Council	Kansas City	MO	\N	\N
Dorchester	Baltimore	MD	\N	\N
Fodor	Columbus	OH	1249	\N
East Pilsen	Chicago	IL	\N	\N
Stonegate	Davis	CA	\N	\N
Kirkside	Kansas City	MO	\N	850
Loring Heights	Atlanta	GA	980	\N
Knoell East	Chandler	AZ	\N	\N
Charles North	Baltimore	MD	\N	\N
Cain Road	Olympia	WA	\N	\N
Bayway Isles	Saint Petersburg	FL	1950	\N
Governor's Square	Charlotte	NC	\N	\N
Eagle Ranch	Fort Worth	TX	\N	\N
Central Business District	Mobile	AL	800	1050
Valentine	Kansas City	MO	\N	\N
Marlborough Mesa	Mesa	AZ	\N	\N
Seton Hill	Baltimore	MD	\N	\N
Hickory Hill	Richmond	VA	\N	\N
Lake Davis-Greenwood	Orlando	FL	\N	\N
Providence Park	Richmond	VA	\N	\N
South Orange	Orlando	FL	\N	\N
Five Points	San Antonio	TX	\N	\N
Guilbeau Park	San Antonio	TX	\N	\N
Stardust Skies Park	Albuquerque	NM	\N	\N
Wheatley Heights	San Antonio	TX	\N	\N
Westlake	Sacramento	CA	\N	1545
Horsethief Canyon Ranch	Corona	CA	\N	1795
Thirteenth St Heights	Saint Petersburg	FL	\N	850
North Roland Park - Poplar Hill	Baltimore	MD	\N	\N
Nineteenth Avenue	San Mateo	CA	\N	\N
Polish Hill	Pittsburgh	PA	\N	\N
Park East	Boulder	CO	\N	1950
Tiburon	Chandler	AZ	\N	\N
Lasalle Park	South Bend	IN	\N	\N
Melrose Heights	Columbia	SC	\N	\N
Downtown	Tampa	FL	1500	\N
Eastern Hills	Fort Worth	TX	\N	\N
Waycroft-Woodlawn	Arlington	VA	\N	\N
Tryon Hills	Charlotte	NC	\N	\N
Southeast Citizens Committee-Highland Park	San Antonio	TX	\N	\N
Baywood	San Mateo	CA	\N	\N
Avondale	Tucson	AZ	\N	600
Peterson Park	Chicago	IL	\N	1800
Ravenswood Gardens	Chicago	IL	\N	1295
Fairfax Village	Washington	DC	\N	\N
Camp Washington	Cincinnati	OH	\N	\N
Mountain View	Tucson	AZ	\N	\N
Country Glenn	Tucson	AZ	\N	895
Compton Heights	Saint Louis	MO	\N	\N
Hayden Island	Portland	OR	\N	\N
Ridgeview	Mesa	AZ	\N	\N
Worthington Village North	Columbus	OH	\N	\N
Castle Hills Forest	San Antonio	TX	\N	\N
Montecito Park	Glendale	CA	\N	\N
North Shearer Hills	San Antonio	TX	\N	\N
Richmond Grove	Sacramento	CA	\N	795
Milbrook	Columbus	OH	\N	575
Balboa Heights	Tucson	AZ	\N	\N
Atlantic Highlands	Jacksonville	FL	\N	\N
Huntington Place	San Antonio	TX	\N	\N
Farmers Market District	Dallas	TX	\N	1370
Mountain First Avenue	Tucson	AZ	\N	\N
Magnolia Heights	Saint Petersburg	FL	\N	\N
Pie Allen	Tucson	AZ	\N	\N
West Dennis	Dennis	MA	\N	\N
Old Southeast	Saint Petersburg	FL	\N	\N
Downtown	Bakersfield	CA	\N	\N
Hollywood	Portland	OR	\N	\N
Robandee South	Kansas City	MO	\N	\N
Rosedale	Mobile	AL	\N	\N
Royal Oaks	Kansas City	MO	\N	\N
Pinehurst	Columbia	SC	\N	\N
Ponderosa-Wingate	Charlotte	NC	\N	\N
University Heights	Tempe	AZ	\N	\N
Rivertown	Detroit	MI	1200	\N
Cottrell Farms	Richmond	VA	\N	\N
Santa Rita Ranch	Mesa	AZ	\N	1275
Shamrock Estates	Gilbert	AZ	\N	\N
Burton Hill Trinity Trails	Fort Worth	TX	\N	\N
Jackson Ward	Richmond	VA	950	1050
Rural-Geneva	Tempe	AZ	\N	\N
Indian Village	Detroit	MI	\N	\N
East Central Park	Orlando	FL	\N	\N
Brice	Columbus	OH	674	\N
Island Station	Milwaukie	OR	\N	870
Manheim Park	Kansas City	MO	\N	\N
Majestic Heights	Boulder	CO	\N	1495
Ocotillo Lakes	Chandler	AZ	\N	\N
Stronghold	Washington	DC	\N	2295
Paschal	Fort Worth	TX	\N	1100
Smallwood	Charlotte	NC	\N	750
Broadmor	Tempe	AZ	\N	\N
Winston-Govans	Baltimore	MD	\N	\N
Irish Hill	Louisville	KY	\N	\N
Mary Munford	Richmond	VA	\N	\N
Harbordale	Saint Petersburg	FL	\N	\N
Cambridge Highlands	Cambridge	MA	\N	2610
Druid Heights	Baltimore	MD	\N	\N
Swan Way Park	Tucson	AZ	\N	\N
Ford City	Chicago	IL	\N	\N
Lesueur Estates	Mesa	AZ	\N	\N
South City Farms	Sacramento	CA	\N	\N
Leisure Lanes	Tulsa	OK	\N	\N
Flushing Meadows Corona Park	New York	NY	\N	\N
Minock Park	Detroit	MI	\N	\N
Adair Park	Atlanta	GA	\N	\N
Keller Park	South Bend	IN	\N	\N
Highland Park	Oakland	CA	\N	\N
Springs	Chandler	AZ	\N	1250
Easterwood	Baltimore	MD	\N	\N
Skyland	Columbia	SC	\N	\N
Canton Industrial Area	Baltimore	MD	\N	\N
Rillito	Tucson	AZ	\N	\N
Kilarney Shores	Jacksonville	FL	615	\N
Casa de Sol	Mesa	AZ	\N	\N
Parkview - Woodbrook	Baltimore	MD	\N	1150
Dos Lagos	Corona	CA	\N	1850
Woodland-Normanstone Terrace	Washington	DC	\N	\N
Flatirons	Boulder	CO	\N	1925
Hughes Acres	Tempe	AZ	\N	\N
Downtown East	Minneapolis	MN	\N	\N
East Chastain Park	Atlanta	GA	1000	1120
Bronx Park	New York	NY	\N	1010
Elm Creek	San Antonio	TX	\N	\N
Kendale	Columbus	OH	\N	\N
Seaboard Industrial	Orlando	FL	\N	\N
Swamp	Jacksonville	FL	\N	\N
Campbell Park	Saint Petersburg	FL	\N	\N
Waverly	Oakland	CA	\N	2800
Wakefield	Baltimore	MD	\N	\N
Franklintown	Baltimore	MD	\N	\N
Limerick	Louisville	KY	\N	\N
Brandon Forest	Charlotte	NC	\N	\N
Signal Butte Ranch	Mesa	AZ	\N	\N
Cibola Addition	Albuquerque	NM	\N	900
Raynolds	Albuquerque	NM	\N	\N
Northpointe	Mesa	AZ	\N	\N
Oak Grove	Richmond	VA	\N	\N
Southland Park	West Palm Beach	FL	\N	\N
Village North One	San Antonio	TX	619	\N
Tiffany	Saint Louis	MO	\N	\N
Grant Park	Tampa	FL	\N	850
Wildwood	Atlanta	GA	\N	\N
Lauderdale Isles	Fort Lauderdale	FL	\N	2495
Samos	Tucson	AZ	\N	900
Beachwood	Jacksonville	FL	\N	\N
Tuttle	Columbus	OH	895	\N
Sherwood	Mesa	AZ	\N	\N
Park Ridge	Jacksonville	FL	\N	\N
Milton - Montford	Baltimore	MD	\N	1000
Berkeley Park	Atlanta	GA	\N	\N
Blackwell	Richmond	VA	\N	\N
Bram's Addition	Town of Madison	WI	\N	\N
Penn Quarter	Washington	DC	2450	2650
Neely Commons	Gilbert	AZ	\N	\N
Highland Groves At Morrison Ranch	Gilbert	AZ	\N	\N
Old Town Manchester	Richmond	VA	\N	\N
Carelton Tract	Sacramento	CA	\N	700
Catalpa Park	Boulder	CO	\N	\N
La Madera	Tucson	AZ	\N	\N
Coventry Hills	Fort Worth	TX	\N	\N
Wilson Park	Baltimore	MD	\N	\N
Cluster - McDonough - Guice	Atlanta	GA	\N	\N
Chisholm Ridge	Fort Worth	TX	\N	1300
Otterbein	Baltimore	MD	1550	\N
Deerwood Center	Jacksonville	FL	\N	\N
Irving	Tulsa	OK	\N	\N
North Downtown	Charlottesville	VA	\N	\N
Fairmount	Richmond	VA	\N	\N
DIA	Denver	CO	\N	\N
Old Westport	Kansas City	MO	899	\N
Highland Pines	Tampa	FL	\N	850
Armory Park	Tucson	AZ	\N	\N
Lake Horney	Lakeland	FL	\N	\N
Brookwood	Atlanta	GA	1077	1245
Calumet Farms	Milwaukee	WI	\N	\N
Valley View	San Bernardino	CA	\N	\N
Wesley Heights	Charlotte	NC	\N	1050
Park Central	Orlando	FL	800	875
Reedy Creek	Richmond	VA	\N	\N
Palmetto Park	Saint Petersburg	FL	\N	850
King William	San Antonio	TX	\N	1450
Tempe Gardens	Tempe	AZ	\N	\N
Rosemary District	Sarasota	FL	\N	2700
Coquina Sands	Naples	FL	\N	4000
Thorpe-Westwood	Spokane	WA	\N	\N
West Village	Detroit	MI	\N	\N
Faircrest	Town of Madison	WI	\N	\N
Darley Park	Baltimore	MD	\N	\N
Coulwood East	Charlotte	NC	\N	\N
Oregon Hill	Richmond	VA	\N	1350
Jefferies	Detroit	MI	\N	\N
Brentwood-Oak Hills	Fort Worth	TX	\N	\N
Union Square	Baltimore	MD	\N	1200
Arbor at Sonoma Ranch	San Antonio	TX	\N	\N
Brookhill	Charlotte	NC	\N	\N
Lewis Mountain	Charlottesville	VA	\N	\N
Eastlake Trails	Chula Vista	CA	\N	2799
Bay Village	Boston	MA	2450	2300
Park Club	Columbus	OH	\N	\N
Fairmount	Wichita	KS	\N	\N
Ashview Heights	Atlanta	GA	\N	850
Oak Haven	Jacksonville	FL	\N	\N
Ashland Ridge	Kansas City	MO	\N	\N
Hamlet	Fort Worth	TX	\N	\N
Broadway Central	Albuquerque	NM	\N	900
Patterson Place	Baltimore	MD	\N	1399
Pinewood Park	West Palm Beach	FL	\N	\N
Flamingo Park	West Palm Beach	FL	\N	\N
Calico Ridge	Henderson	NV	\N	1695
Gateway Ranch	Gilbert	AZ	\N	\N
Neely Farms	Gilbert	AZ	\N	\N
Washington Park	Atlanta	GA	\N	\N
Cookes Meadow	Fort Worth	TX	\N	\N
Peachtree Park	Atlanta	GA	1220	\N
Colonialtown South	Orlando	FL	\N	\N
Campbell-Grant	Tucson	AZ	\N	\N
Northwest	Tucson	AZ	\N	\N
Oakmont	Glendale	CA	\N	\N
Sunrise Intracoastal	Fort Lauderdale	FL	\N	2300
Rolling Hills	Jackson	MS	\N	\N
Lake Euclid	Saint Petersburg	FL	\N	\N
Lakewood	Atlanta	GA	\N	\N
Mitman	Tucson	AZ	\N	\N
Westminster Heights	Saint Petersburg	FL	\N	850
Oakenshawe	Baltimore	MD	\N	\N
Union Hill	Richmond	VA	644	825
Girdwood	Anchorage	AK	\N	\N
Greektown	Chicago	IL	\N	2000
McKinley Heights	Saint Louis	MO	\N	\N
The Villages at East Lake	Atlanta	GA	\N	\N
Columbus Square	Saint Louis	MO	\N	\N
Rose Hill	Charlottesville	VA	\N	\N
Port Royal	Naples	FL	\N	\N
Optimist Park	Charlotte	NC	\N	1144
Iuka Ravine	Columbus	OH	\N	800
San Miguel Ranch	Chula Vista	CA	\N	\N
Mount Holly	Baltimore	MD	\N	\N
Pleasant Valley	Mobile	AL	\N	\N
Saybrook Manor	Old Saybrook	CT	\N	\N
Rosemont Homeowners-Tenants	Baltimore	MD	\N	1200
West Shore Palms	Tampa	FL	\N	\N
City Center District	Dallas	TX	\N	1560
Gould Park	Columbus	OH	\N	\N
The Vineyards at Heritage	Fort Worth	TX	\N	1325
Riverside	Atlanta	GA	1350	750
Royal Palms	Mesa	AZ	\N	\N
Butchertown	Louisville	KY	\N	1100
Spencer Lakes	West Palm Beach	FL	\N	\N
Carpenter-Ridgeway	Town of Madison	WI	\N	\N
Northeast	Alexandria	VA	1965	\N
Croatan Beach	Virginia Beach	VA	\N	\N
Southgate	Fort Worth	TX	\N	1145
Carroll Heights	Atlanta	GA	\N	\N
Poynter Crossing	Fort Worth	TX	\N	1195
Edgewood	Lakeland	FL	\N	\N
Pineloch	Orlando	FL	\N	900
Dillard Park	Fort Lauderdale	FL	1575	\N
Gaslamp Quarter	San Diego	CA	1995	2550
Northcrest	Fort Wayne	IN	\N	\N
Cameron Village	Baltimore	MD	\N	\N
Palestine West and Oak Park Northeast	Kansas City	MO	\N	\N
Lido Key	Sarasota	FL	3800	3800
FNW	South Bend	IN	\N	\N
Concerned Citizens of Forest Park	Baltimore	MD	\N	\N
Chippenham Forest	Richmond	VA	\N	\N
Plaza Westport	Kansas City	MO	1300	1195
Crosswinds Colony	Saint Petersburg	FL	753	737
Garden City	Jacksonville	FL	\N	\N
Maple-Ash	Tempe	AZ	\N	\N
Good Hope	Washington	DC	\N	\N
Carillon	Saint Petersburg	FL	1390	1580
Fox Run	Fort Worth	TX	\N	\N
Woodlawn Oaks	Saint Petersburg	FL	\N	\N
Cherokee Park	Nashville	TN	\N	\N
Metro Center	Sacramento	CA	\N	\N
Maywood	Arlington	VA	\N	\N
Country Club Plaza	Kansas City	MO	\N	1850
Marlborough East	Kansas City	MO	\N	\N
Alkali Flat	Sacramento	CA	\N	950
Shady Banks	Fort Lauderdale	FL	\N	1850
Stonecreek	Gilbert	AZ	\N	\N
Netherwood Park	Albuquerque	NM	\N	\N
Shady Canyon	Irvine	CA	\N	\N
Candle Ridge West	Fort Worth	TX	\N	1250
Silverwood	Charlotte	NC	\N	\N
River Run	Fort Lauderdale	FL	\N	\N
Pioneer Square	Seattle	WA	\N	\N
Lake Point Condominiums	Garland	TX	505	\N
Arsenal Hill	Columbia	SC	\N	\N
Capitol Neighbors	Jackson	MS	\N	\N
Stuart	Kalamazoo	MI	\N	\N
Hudson Manor	Tempe	AZ	725	\N
Pumpkin Hill	Jacksonville	FL	\N	1352
Mockingbird Hill	San Antonio	TX	\N	\N
Marine Creek	Fort Worth	TX	\N	1325
Las Olas Isles	Fort Lauderdale	FL	1950	5500
North Orange	Orlando	FL	\N	1485
Reston Heights	Town of Madison	WI	\N	\N
Lauderdale West	Fort Lauderdale	FL	1600	\N
Greenmount West	Baltimore	MD	\N	\N
Revolution Park	Charlotte	NC	\N	\N
Forest Crest	San Antonio	TX	\N	2350
Rancho Encantado	San Diego	CA	\N	\N
Abell	Baltimore	MD	\N	\N
Easton	Columbus	OH	\N	\N
South Poinsettia	Sarasota	FL	\N	\N
Gold Coast	Detroit	MI	\N	\N
Eastridge Estates	Bakersfield	CA	\N	975
UNITE	South Bend	IN	\N	\N
Gateway	Austin	TX	978	\N
Oldham Farms	Kansas City	MO	\N	\N
South Lake Worth	Fort Worth	TX	\N	\N
Near East Side	Fort Worth	TX	\N	\N
MacArthur Park	San Antonio	TX	\N	\N
Ridgestone	San Antonio	TX	\N	\N
Blandtown	Atlanta	GA	\N	1241
Perkins	Saint Petersburg	FL	\N	\N
Clayton Heights-Lomas del Cielo	Albuquerque	NM	1099	\N
Woodbourne-McCabe	Baltimore	MD	\N	\N
Southern Manor I and II	Mesa	AZ	\N	\N
The Woodlands	Nashville	TN	\N	\N
Ivanhoe Northeast	Kansas City	MO	\N	\N
Fitzsimons	Aurora	CO	1350	\N
Thunderbird Heights-Wilmot Desert Estates	Tucson	AZ	\N	\N
Baseline-Hardy	Tempe	AZ	758	\N
Woodlake	Sacramento	CA	\N	\N
Northwood Shores	West Palm Beach	FL	\N	2000
The Vineyard	San Antonio	TX	\N	\N
Southern Barton Heights	Richmond	VA	\N	875
Chinatown	Washington	DC	\N	2390
Wildwood	Charlotte	NC	\N	\N
Cabbagetown	Atlanta	GA	\N	\N
Historic Third Ward	Milwaukee	WI	1545	1500
Pleasant Hill	Washington	DC	\N	\N
Visitation Park	Saint Louis	MO	\N	790
Table Mesa North	Boulder	CO	\N	1359
Sunrise	Davis	CA	\N	\N
Bay Colony	Fort Lauderdale	FL	\N	\N
Kelly Town-Rugby Heights	Charlottesville	VA	\N	\N
Mesquite Ranch	Tucson	AZ	\N	\N
Bluebonnet Hills	Fort Worth	TX	\N	1250
Boulder Creek	Mesa	AZ	\N	\N
Antelope Run	Albuquerque	NM	\N	\N
McClintock	Tempe	AZ	\N	\N
Broadway Gillham	Kansas City	MO	460	689
North Shore	West Palm Beach	FL	\N	\N
Chula Vista	Fort Lauderdale	FL	\N	\N
Enatai	Bellevue	WA	\N	\N
Broad Rock	Richmond	VA	\N	\N
San Joaquin Marsh	Irvine	CA	\N	\N
Sunset Hill	Kansas City	MO	625	\N
Grandview Heights	West Palm Beach	FL	\N	\N
Clarendon Heights	San Francisco	CA	\N	\N
Cherry	Charlotte	NC	\N	\N
Glencliff Estates	Nashville	TN	\N	795
Old Northwood	West Palm Beach	FL	\N	1550
Grant Creek	Missoula	MT	\N	850
Crown Pointe	Lincoln	NE	\N	\N
East Bank-Nicollet Island	Minneapolis	MN	\N	\N
Colee Hammock	Fort Lauderdale	FL	2300	1550
Chestnut Hill Plantation	Columbia	SC	\N	1400
Bluebonnet Place	Fort Worth	TX	\N	850
Pleasant City	West Palm Beach	FL	\N	\N
Stone Oak Communities of Mutual Amenities-Stone Oak	San Antonio	TX	\N	\N
Creek Hollow Estates	Richardson	TX	\N	\N
Downtown	Charlottesville	VA	\N	\N
Quail Hill	Irvine	CA	2800	2850
Five Points	Saint Petersburg	FL	\N	\N
El Cid	West Palm Beach	FL	\N	\N
South Hill	Grand Rapids	MI	\N	\N
McGuire	Richmond	VA	\N	\N
Twinlakes	Fort Lauderdale	FL	\N	\N
River Walk	West Palm Beach	FL	\N	1900
Shalimar	Tempe	AZ	\N	\N
Portola Springs	Irvine	CA	\N	2365
Park Place	San Antonio	TX	\N	\N
Wilson Heights	Baltimore	MD	\N	\N
Meridian Hills	Mesa	AZ	\N	\N
Frisco Heights	Fort Worth	TX	\N	1595
Union Hill	Kansas City	MO	1320	\N
Orchard Knob	Atlanta	GA	\N	\N
Government District	Dallas	TX	1096	\N
Hogan	Jacksonville	FL	\N	\N
East Industrial	Fremont	CA	\N	\N
West Byers	Fort Worth	TX	\N	\N
Lauderdale Beach	Fort Lauderdale	FL	3000	4950
Polaris North	Columbus	OH	\N	929
Haymarket	Boston	MA	\N	3100
Lake Nona South	Orlando	FL	\N	\N
Wydown-Skinker	Saint Louis	MO	1070	\N
Auraria	Denver	CO	\N	\N
BRSC	Charlottesville	VA	\N	\N
Manchester	Richmond	VA	\N	995
Lithuanian Plaza	Chicago	IL	\N	\N
Arizona Skyline	Mesa	AZ	\N	\N
Cromwell Heights	Saint Petersburg	FL	\N	\N
Sunburst	Aurora	CO	\N	\N
Cheltenham	Saint Louis	MO	\N	\N
Niskey Lake	Atlanta	GA	\N	\N
Clark Park	Tempe	AZ	\N	\N
Junction Ridge	Town of Madison	WI	\N	\N
Capitol Gateway	Atlanta	GA	1000	\N
Palm Aire Village (WEST)	Fort Lauderdale	FL	\N	\N
Kempton Crossing	Chandler	AZ	\N	1450
Rockdale	Atlanta	GA	\N	\N
The Gardens	Gilbert	AZ	\N	1150
Main Street District	Dallas	TX	\N	1350
Central Office	Richmond	VA	\N	1400
Santa Rita Park	Tucson	AZ	\N	650
Brakridge	Jacksonville	FL	\N	\N
Tyrone Landing	Saint Petersburg	FL	\N	\N
Coliseum-Willow Park	San Antonio	TX	\N	\N
Cooley Station North	Gilbert	AZ	\N	\N
Higley Park	Gilbert	AZ	\N	\N
Marilyn Ann	Tempe	AZ	\N	\N
Home Beautiful Park	Fort Lauderdale	FL	\N	\N
Pasadena Vista	Saint Petersburg	FL	\N	\N
Downtown Core	Davis	CA	\N	\N
Alhambra Triangle	Sacramento	CA	\N	\N
Lauderdale Harbours	Fort Lauderdale	FL	1600	\N
Beverly Heights	Fort Lauderdale	FL	2000	1750
Richnor Springs	Baltimore	MD	\N	\N
Starr Pass	Tucson	AZ	\N	\N
English Village	Detroit	MI	\N	\N
Community at Bordeaux	Nashville	TN	\N	\N
Dolphin Isles	Fort Lauderdale	FL	2500	\N
Heart of Italy	Chicago	IL	\N	\N
Liberty Park	Jersey City	NJ	\N	\N
West End Park	Nashville	TN	\N	1525
The Crossing of Fossil Creek	Fort Worth	TX	\N	\N
Crown Center	Kansas City	MO	1400	\N
Glebewood	Arlington	VA	\N	2745
Mays	Atlanta	GA	\N	\N
Rudee Heights	Virginia Beach	VA	\N	1350
West End Historic District	Dallas	TX	\N	1063
Harbour Inlet	Fort Lauderdale	FL	1957	1300
Seven Isles	Fort Lauderdale	FL	6300	17500
Central Park	West Palm Beach	FL	\N	1600
NTNA - West Rio	Tempe	AZ	\N	950
Lake Richmond	Orlando	FL	\N	\N
Thornton Park	Orlando	FL	\N	\N
Joyland	Atlanta	GA	640	\N
Laurel Hill Valley	Eugene	OR	\N	\N
Mitchell Park East	Tempe	AZ	\N	\N
Strip District	Pittsburgh	PA	1200	\N
St. Armands	Sarasota	FL	\N	6500
Mission Hills Condominium Association	Clearwater	FL	\N	\N
Vincenz	Gilbert	AZ	\N	\N
Ridglea	Fort Worth	TX	\N	\N
Carillon	Richmond	VA	\N	\N
Northpointe	Jackson	MS	765	\N
Brentwood-Cavalier	Tempe	AZ	\N	\N
Crimson Creek	Mesa	AZ	\N	1150
Aqualane Shore	Naples	FL	\N	\N
Midland Terrace	Columbia	SC	\N	\N
Concord Village	Mesa	AZ	\N	\N
Silk Stocking	Chandler	AZ	\N	\N
Gateway Village	Gilbert	AZ	\N	\N
Remington Point	Fort Worth	TX	\N	1200
The Meadows	Charlottesville	VA	\N	\N
The Ranches	Fort Worth	TX	\N	1400
Richland Heights West	Tucson	AZ	\N	\N
Swallow Circle - Baywood	Atlanta	GA	\N	\N
Oeste Manor	Davis	CA	\N	\N
Elmwood Park	Columbia	SC	\N	\N
Meridian Pointe	Mesa	AZ	\N	\N
Commonwealth	Charlotte	NC	\N	\N
Ray Ranch	Gilbert	AZ	\N	\N
5 Points	Sarasota	FL	4000	\N
Channing Valley	Atlanta	GA	\N	\N
Booth-Boyd	Baltimore	MD	\N	\N
Scott's Addition	Richmond	VA	\N	\N
Downtown Crossing	Boston	MA	\N	2300
Locust Point	Baltimore	MD	\N	1900
Deerwood	Atlanta	GA	\N	\N
Jacksonville North Estate	Jacksonville	FL	\N	\N
Westland	Fort Worth	TX	\N	\N
Village 5	Sacramento	CA	\N	1089
Crownridge of Texas Owners Association	San Antonio	TX	\N	\N
McClintock Manor	Tempe	AZ	\N	865
Windhover	Orlando	FL	\N	875
The Wells	Mesa	AZ	\N	\N
Blossom Park	San Antonio	TX	\N	\N
Signal Butte Manor	Mesa	AZ	\N	\N
Florida Heights	Atlanta	GA	\N	\N
The Parks of Deer Creek	Fort Worth	TX	\N	1300
City Center	Richmond	VA	\N	1125
Lake Estates	Fort Lauderdale	FL	\N	\N
Murphy Creek	Aurora	CO	\N	\N
Whittier Mill Village	Atlanta	GA	\N	\N
Marine Creek Hills	Fort Worth	TX	\N	1150
Northwoods	Columbus	OH	\N	\N
Boulevard Heights	Atlanta	GA	\N	\N
Big Bayou	Saint Petersburg	FL	\N	\N
Germantown	Nashville	TN	\N	1520
Ridgely Delight	Baltimore	MD	\N	\N
North Golf Estates	Fort Lauderdale	FL	900	1000
McGuire Veterans Hospital	Richmond	VA	720	\N
Heather Place	Chandler	AZ	\N	\N
Idlewyld	Fort Lauderdale	FL	2155	2500
Encino Ranch	San Antonio	TX	\N	\N
Vinegar Hill	New York	NY	\N	3738
Bal Harbour	Fort Lauderdale	FL	\N	\N
Joseph Lee	Baltimore	MD	\N	\N
Hendricks and Venice Isles	Fort Lauderdale	FL	2500	2150
Sandbridge	Virginia Beach	VA	\N	1300
Harbour Isles	Fort Lauderdale	FL	2450	3000
Northboro Park	West Palm Beach	FL	\N	\N
Hibiscus Island	Miami Beach	FL	\N	12000
Lake Caroline	Dallas	TX	\N	\N
Willows	Gilbert	AZ	\N	1199
Blair Villa - Poole Creek	Atlanta	GA	\N	\N
Lake Nona Central	Orlando	FL	\N	1650
River Market	Kansas City	MO	1100	1250
El Toro Marine Air Station	Irvine	CA	1895	2155
Herman Gardens	Detroit	MI	\N	\N
North Shore	Pittsburgh	PA	\N	\N
Arts District	Dallas	TX	\N	\N
Biscayne Island	Miami	FL	\N	\N
Bridgepointe	San Mateo	CA	\N	2791
Sunshine Valley	Chandler	AZ	\N	\N
East Pyron - Symphony Lane-Mission San Jose	San Antonio	TX	\N	\N
Val Vista Classic	Gilbert	AZ	\N	1195
Eagle Glen	Corona	CA	\N	\N
Elmco Estates	Atlanta	GA	\N	\N
Woodland Hills	Atlanta	GA	\N	\N
Palm-Aire Village (EAST)	Fort Lauderdale	FL	\N	1100
Palm Island	Miami Beach	FL	\N	37500
Sycamore Creek	Corona	CA	\N	2250
Bay Colony Club	Fort Lauderdale	FL	\N	1350
Monterey Vista	Chandler	AZ	\N	\N
Pineapple Park	West Palm Beach	FL	\N	\N
Riviera Isles	Fort Lauderdale	FL	\N	\N
Oak Highlands	Nashville	TN	\N	\N
Capitol Hill Area	Nashville	TN	705	\N
Randall Mill	Atlanta	GA	\N	\N
La Salle	Saint Louis	MO	\N	\N
Iron Horse	Tucson	AZ	\N	\N
Merit-Carson	Torrance	CA	\N	\N
Rebel Valley Forest	Atlanta	GA	\N	\N
Willow Creek	Tulsa	OK	\N	\N
Coral Shores	Fort Lauderdale	FL	\N	1200
Golden Gate Point	Sarasota	FL	\N	\N
Fair Isle	Miami	FL	\N	\N
Rock Island - Samuels	Fort Worth	TX	\N	\N
Thousand Oaks Condominiums-Thousand Oaks	San Antonio	TX	\N	\N
Vista Dorada	Gilbert	AZ	\N	\N
Keewaydin	Boulder	CO	\N	\N
Laudergate Isles	Fort Lauderdale	FL	\N	\N
San Marco Island	Miami	FL	\N	\N
West End	Pittsburgh	PA	\N	\N
Tantra Park	Boulder	CO	\N	\N
Cooley Station	Gilbert	AZ	\N	\N
Lost Creek	Fort Worth	TX	\N	925
John Cox	Lakeland	FL	\N	\N
University Estates	Tempe	AZ	\N	\N
Raintree	Lakeland	FL	\N	\N
Pershing	Orlando	FL	\N	\N
Di Lido Island	Miami Beach	FL	\N	10000
Fincher Farms	Gilbert	AZ	\N	\N
Van Cortlandt Park	New York	NY	\N	1250
Birch Park Finger Sts.	Fort Lauderdale	FL	\N	\N
Woodlawn West	Nashville	TN	\N	\N
The Willows	Orlando	FL	\N	\N
Provincia Villas	San Antonio	TX	\N	\N
Colonial Homes	Atlanta	GA	\N	\N
Maverick Creek	San Antonio	TX	\N	\N
Downtown	Columbia	SC	\N	925
Oakwood	Richmond	VA	\N	\N
Oakland	Atlanta	GA	\N	\N
Lennox Village	Nashville	TN	\N	\N
Eden Isle	Saint Petersburg	FL	\N	\N
Charleston Commons	Garland	TX	\N	\N
Buena Vista	Boulder	CO	1469	\N
Rosemont East	Tucson	AZ	\N	\N
Upper West Side	Fort Worth	TX	\N	\N
Woodland Point	Nashville	TN	\N	760
Leather District	Boston	MA	\N	3000
Seville Condo No.11	Clearwater	FL	850	1185
Westhampton Dunes	Westhampton Beach	NY	65000	53900
Stratland Shadows	Gilbert	AZ	\N	\N
San Antonio Cambridge Village-East Terrell Hills	San Antonio	TX	\N	\N
City View Townhome	Fort Lauderdale	FL	\N	\N
Windmill Ranch	Gilbert	AZ	\N	\N
Northlake Park at Lake Nona	Orlando	FL	\N	1500
Devonshire Condominiums	San Antonio	TX	\N	\N
La Aldea	Gilbert	AZ	\N	\N
Fleetwood	Nashville	TN	695	\N
Wyngate Townhomes	Saint Petersburg	FL	\N	\N
Breakwater Surf	Fort Lauderdale	FL	3500	\N
Grandview Estates	Mesa	AZ	\N	\N
Pecos Manor	Gilbert	AZ	\N	\N
Solana Ridge Homeowners - People Active in Community Effort	San Antonio	TX	\N	\N
East Park	Orlando	FL	\N	1500
Third Cherry Creek	Aurora	CO	\N	\N
Summit at Bulverde Creek	San Antonio	TX	\N	\N
LaVina	Orlando	FL	\N	1395
Green Meadows	Davis	CA	\N	\N
Alta Loma	Nashville	TN	\N	615
Navy Yard	New York	NY	\N	\N
Woodmont	San Antonio	TX	\N	\N
Singletree	Aurora	CO	\N	\N
La Buena Vida	Davis	CA	\N	\N
Oakdell Council of Co-Owners	San Antonio	TX	\N	\N
Prospect Park	New York	NY	\N	\N
Hillcrest	Hollywood	FL	\N	1000
North Weymouth	Weymouth	MA	\N	1200
Kennydale	Renton	WA	\N	1695
Mountain View	Bend	OR	\N	\N
Washington Park	Hollywood	FL	\N	1350
Ponderosa	Sunnyvale	CA	\N	2250
North Beach	Hollywood	FL	\N	3500
Nicholtown	Greenville	SC	\N	\N
Sunset	Renton	WA	\N	1250
Princess Anne Plaza	Virginia Beach	VA	\N	995
Washington	Sunnyvale	CA	\N	2700
Beverly Park	Hollywood	FL	\N	1350
Boulevard Heights	Hollywood	FL	\N	1500
Driftwood	Hollywood	FL	\N	1600
Emerald Hills	Hollywood	FL	\N	1800
Hollywood Hills	Hollywood	FL	\N	1750
Hollywood Lakes	Hollywood	FL	\N	2300
Lawnacres	Hollywood	FL	\N	1200
Liberia	Hollywood	FL	\N	1350
Mapleridge	Hollywood	FL	\N	2400
Oakridge	Hollywood	FL	\N	2600
Park East	Hollywood	FL	\N	1595
Park Side	Hollywood	FL	\N	1250
Royal Poinciana	Hollywood	FL	\N	1050
East Village	San Marino	CA	\N	\N
Lakewood	Sunnyvale	CA	\N	2750
Cascade	Renton	WA	1215	\N
Governors Island	New York	NY	\N	2930
North Shore	Miami Beach	FL	\N	2400
Riverside	Greenwich	CT	\N	7500
Oakrest Condos	Nashville	TN	\N	\N
River Reach	Naples	FL	\N	\N
Boyd Acres	Bend	OR	\N	\N
South Renton	Renton	WA	\N	\N
Leisure Estates	Renton	WA	\N	\N
President Park	Renton	WA	\N	1350
Old Farm District	Bend	OR	\N	1200
Larksput	Bend	OR	\N	\N
Awbrey Butte	Bend	OR	\N	\N
River West	Bend	OR	\N	925
Summit West	Bend	OR	\N	\N
Century West	Bend	OR	\N	\N
Southwest Bend	Bend	OR	\N	\N
Southern Crossing	Bend	OR	\N	\N
Old City	Philadelphia	PA	\N	1700
Carriage	Hollywood	FL	\N	\N
Playland	Hollywood	FL	\N	1500
441 Corridor	Hollywood	FL	\N	1200
Lake of Emerald Hills	Hollywood	FL	\N	1975
North Central	Hollywood	FL	\N	1175
Highland Garden	Hollywood	FL	\N	1400
South Central Beach	Hollywood	FL	\N	2300
Oceanfront	Miami Beach	FL	\N	2600
Nautilus	Miami Beach	FL	\N	2600
South Pointe	Miami Beach	FL	\N	4500
Serra	Sunnyvale	CA	\N	2494
Ortega	Sunnyvale	CA	\N	2257
De Anza	Sunnyvale	CA	\N	\N
East Murphy	Sunnyvale	CA	\N	2389
West Murphy	Sunnyvale	CA	\N	2250
Sharon Heights	Menlo Park	CA	\N	4200
Downtown Menlo Park	Menlo Park	CA	\N	\N
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

