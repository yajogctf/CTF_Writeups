from Crypto.Util.number import long_to_bytes

n1 = 16895844090302140592659203092326754397916615877156418083775983326567262857434286784352755691231372524046947817027609871339779052340298851455825343914565349651333283551138205456284824077873043013595313773956794816682958706482754685120090750397747015038669047713101397337825418638859770626618854997324831793483659910322937454178396049671348919161991562332828398316094938835561259917841140366936226953293604869404280861112141284704018480497443189808649594222983536682286615023646284397886256209485789545675225329069539408667982428192470430204799653602931007107335558965120815430420898506688511671241705574335613090682013
e1 = 65537
c1 = 7818321254750334008379589501292325137682074322887683915464861106561934924365660251934320703022566522347141167914364318838415147127470950035180892461318743733126352087505518644388733527228841614726465965063829798897019439281915857574681062185664885100301873341937972872093168047018772766147350521571412432577721606426701002748739547026207569446359265024200993747841661884692928926039185964274224841237045619928248330951699007619244530879692563852129885323775823816451787955743942968401187507702618237082254283484203161006940664144806744142758756632646039371103714891470816121641325719797534020540250766889785919814382

n2 = 22160567763948492895090996477047180485455524932702696697570991168736807463988465318899280678030104758714228331712868417831523511943197686617200545714707332594532611440360591874484774459472586464202240208125663048882939144024375040954148333792401257005790372881106262295967972148685076689432551379850079201234407868804450612865472429316169948404048708078383285810578598637431494164050174843806035033795105585543061957794162099125273596995686952118842090801867908842775373362066408634559153339824637727686109642585264413233583449179272399592842009933883647300090091041520319428330663770540635256486617825262149407200317
e2 = 65537
c2 = 19690520754051173647211685164072637555800784045910293368304706863370317909953687036313142136905145035923461684882237012444470624603324950525342723531350867347220681870482876998144413576696234307889695564386378507641438147676387327512816972488162619290220067572175960616418052216207456516160477378246666363877325851823689429475469383672825775159901117234555363911938490115559955086071530659273866145507400856136591391884526718884267990093630051614232280554396776513566245029154917966361698708629039129727327128483243363394841238956869151344974086425362274696045998136718784402364220587942046822063205137520791363319144

n3 = 30411521910612406343993844830038303042143033746292579505901870953143975096282414718336718528037226099433670922614061664943892535514165683437199134278311973454116349060301041910849566746140890727885805721657086881479617492719586633881232556353366139554061188176830768575643015098049227964483233358203790768451798571704097416317067159175992894745746804122229684121275771877235870287805477152050742436672871552080666302532175003523693101768152753770024596485981429603734379784791055870925138803002395176578318147445903935688821423158926063921552282638439035914577171715576836189246536239295484699682522744627111615899081
e3 = 65537
c3 = 17407076170882273876432597038388758264230617761068651657734759714156681119134231664293550430901872572856333330745780794113236587515588367725879684954488698153571665447141528395185542787913364717776209909588729447283115651585815847333568874548696816813748100515388820080812467785181990042664564706242879424162602753729028187519433639583471983065246575409341038859576101783940398158000236250734758549527625716150775997198493235465480875148169558815498752869321570202908633179473348243670372581519248414555681834596365572626822309814663046580083035403339576751500705695598043247593357230327746709126221695232509039271637


# https://www.dcode.fr/decomposition-nombres-premiers (comma separated factors)
p1 = 129984014749130366259742130443330376923069118727641845190136006048911945242427603092160936004682857611235008521722596025476170673607376869837675885556290582081941522328978811710862857253777650447221864279732376499043513950683086803379743964370215090077032772967632331576620201195241241611325672953583711295127
q1 = 129984014749130366259742130443330376923069118727641845190136006048911945242427603092160936004682857611235008521722596025476170673607376869837675885556290582081941522328978811710862857253777650447221864279732376499043513950683086803379743964370215090077032772967632331576620201195241241611325672953583711299819
phi1 = (p1 - 1) * (q1 - 1)
d1 = pow(e1, -1, phi1)
pt1 = pow(c1, d1, n1)

# https://www.dcode.fr/decomposition-nombres-premiers (comma separated factors)
p2 = 126533202039063001896688053184317501172861811900329909666064784398827845308206133665757830643454305851333401419985380438047719101436355025080050331120723599519253947046227257916602963852707478694031635261891164331924972408163445583347008941375632757240181207729214090528397599635041325648341162091757870321551
q2 = 175136386393724074897068211302311758514344898633187862983126380556807924872210372704023620020763131468811275018725481764101835410780850364387004844957680252860643364609959757601263568806626614487575229052115194838589297358422557307359118854093864998895206960681533165623745478696564104830629591040860031236467
phi2 = (p2 - 1) * (q2 - 1)
d2 = pow(e1, -1, phi2)
pt2 = pow(c2, d2, n2)

# https://www.dcode.fr/decomposition-nombres-premiers (comma separated factors)
p3 = 173644794989913004576326487170453027208749262944819613516113347012140336172500489057423935036024776789926767263206394459648963430015169908275849860588106163038132274416249962212228685370880392724406366338349372748063119599008792942728381354056134718729175590402854387508408159461560446661505593588717183993043 
q3 = 175136386393724074897068211302311758514344898633187862983126380556807924872210372704023620020763131468811275018725481764101835410780850364387004844957680252860643364609959757601263568806626614487575229052115194838589297358422557307359118854093864998895206960681533165623745478696564104830629591040860031236467
phi3 = (p3 - 1) * (q3 - 1)
d3 = pow(e3, -1, phi3)
pt3 = pow(c3, d3, n3)

print(long_to_bytes(pt1).decode() + long_to_bytes(pt2).decode() + long_to_bytes(pt3).decode())