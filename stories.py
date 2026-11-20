"""The stories on the 19 November 2026 front page. Every item is dated 19 Nov by its source (research.md)."""

LEADS = [
    dict(region='ASIA', place='Shenzhen', field='summit', icon='summit', lon=114, lat=22.5, src='Democracy Now, CNBC',
         head='Trump, Xi and Putin hold the first three-way summit',
         dek='90 minutes at APEC; Chinese media hail a four-point "peace declaration": nuclear risk, oil refining, UN reform, curbs on the ICC.'),
    dict(region='ASIA', place='The Hague', field='justice', icon='scales', lon=96, lat=20, src='Al Jazeera, Amnesty',
         head='UN court rules Myanmar committed genocide',
         dek='By 9 votes to 6 the ICJ finds Myanmar responsible for genocide against the Rohingya in 2016-17. The ruling is final.'),
    dict(region='AMERICAS', place='New York', field='markets', icon='stock', lon=-74, lat=40.7, src='CNN, Bloomberg',
         head='Anthropic jumps 17% on debut as Dow sheds 1,101',
         dek='Priced at $83, opened at $111.50, closed $97.17 in the largest IPO on record; S&P 500 falls 2% for a sixth straight loss.'),
]

SECOND = [
    dict(region='EUROPE', place='Kerch', field='war', icon='bridge', lon=36.5, lat=45.3, src='AP',
         head='Third strike in four days halts Crimea bridge trains', dek='Russia says it downed 53 drones overnight.'),
    dict(region='EUROPE', place='Copenhagen', field='Arctic', icon='arctic', lon=12.6, lat=55.7, src='Al Jazeera',
         head='Denmark ratifies US-Greenland security pact', dek='Parliament votes 109-0.'),
    dict(region='MIDDLE EAST', place='Riyadh', field='war', icon='missile', lon=46.7, lat=24.7, src='Al Jazeera',
         head='Houthi missile debris hits Riyadh tower', dek='No injuries; Saudi strikes on Sanaa follow.'),
    dict(region='ASIA', place='Seoul', field='justice', icon='gavel', lon=127, lat=37.5, src='AP',
         head="Top court overturns ex-PM Han's conviction", dek='Martial-law case sent back for resentencing.'),
    dict(region='ASIA', place='Ulaanbaatar', field='politics', icon='vote', lon=106.9, lat=47.9, src='AP',
         head="Mongolia's parliament accepts president's resignation", dek='96 of 104 MPs vote yes.'),
    dict(region='GLOBAL', place='Antalya', field='COP31', icon='climate', lon=30.7, lat=36.9, src='UN News',
         head='COP31 draft drops all fossil-fuel language', dek='Revised text halved; talks due to end Friday.'),
    dict(region='GLOBAL', place='Worldwide', field='games', icon='game', lon=None, lat=None, src='Rockstar',
         head='Grand Theft Auto VI goes on sale', dek='Midnight launch rolls round the world.'),
    dict(region='AFRICA', place='Mogadishu', field='diplomacy', icon='expel', lon=45.3, lat=2, src='Reuters',
         head='Somalia orders UAE ambassador out', dek='72 hours to leave over "open invasion".'),
    dict(region='OCEANIA', place='Canberra', field='economy', icon='jobs', lon=149, lat=-35.3, src='ABC',
         head='Australian jobless rate jumps to 4.9%', dek='Highest since 2021; 43,500 jobs lost.'),
    dict(region='ASIA', place='Odisha', field='storm', icon='cyclone', lon=85.8, lat=20.3, src='Deccan Herald',
         head='105,000 evacuated as Cyclone Akvan nears India', dek='Landfall expected Friday.'),
]

ALSO = [
    dict(region='EUROPE', place='Berlin', text='Zelensky meets US envoys, 40+ allies', src='Kyiv Independent', lon=13.4, lat=52.5),
    dict(region='AFRICA', place='Dakar', text='President imposes budget by decree', src='AFP', lon=-17.4, lat=14.7),
    dict(region='AMERICAS', place='Bogota', text='National strike against tax reform', src='Infobae', lon=-74, lat=4.7),
    dict(region='AFRICA', place='Nairobi', text='Jepchirchir banned three years for EPO', src='Al Jazeera', lon=36.8, lat=-1.3),
    dict(region='EUROPE', place='Brussels', text='EU Commission hit by AI-aided hack', src='Notebookcheck', lon=4.4, lat=50.8),
    dict(region='ASIA', place='Manila', text='Philippines and Chile sign trade pact', src='Inquirer', lon=121, lat=14.6),
    dict(region='MIDDLE EAST', place='Hormuz', text='Iran says two tankers hit mines', src='Anadolu', lon=56.5, lat=26.3),
    dict(region='GLOBAL', place='IEA', text='Outlook: emissions hit record 54.1 Gt', src='IEA', lon=28, lat=38),
    dict(region='OCEANIA', place='Wellington', text='Court: pay-equity law breached rights', src='1News', lon=174.8, lat=-41.3),
    dict(region='GLOBAL', place='FIFA', text='Two rivals to challenge Infantino', src='Al Jazeera', lon=8.5, lat=47.4),
    dict(region='OCEANIA', place='Wellington', text='Nicholls 113* rescues NZ v India', src='Gulf News', lon=174.6, lat=-41.1),
    dict(region='ASIA', place='Gopalganj', text='Police station torched in Bangladesh', src='Dhaka Tribune', lon=89.8, lat=23),
    dict(region='MIDDLE EAST', place='Bekaa', text='Israel strikes Hezbollah missile site', src='Times of Israel', lon=36, lat=33.8),
    dict(region='MIDDLE EAST', place='Dahi', text='Mosque set on fire in northern Israel', src='Al Jazeera', lon=35.4, lat=32.6),
    dict(region='MIDDLE EAST', place='Gaza', text='Hospital chief held six more months', src='Democracy Now', lon=34.4, lat=31.5),
    dict(region='AMERICAS', place='FDA', text='Lung-cancer drug neladalkib approved', src='MSK', lon=-77, lat=39),
    dict(region='AMERICAS', place='Vandenberg', text='SpaceX scrubs Space Force launch', src='Spaceflight Now', lon=-120.6, lat=34.7),
]

FIGURES = [
    ('3', 'leaders, one table'), ('9–6', 'ICJ genocide vote'), ('$97.17', "Anthropic's first close"),
    ('−1,101', 'Dow points lost'), ('109–0', 'Danish vote on Greenland'), ('4.9%', 'Australian jobless rate'),
]

DATE_CHECK = ('Every story here happened, or was first reported, on Thursday 19 November 2026. Left out as other '
              "days' news: 18 Nov - US-Venezuela military pact, Iran's strikes on Kuwait and Bahrain, the EU's "
              "Ukraine loan plan; 17 Nov - Nvidia's results; 20 Nov - Cyclone Akvan's landfall and COP31's close.")

SOURCES = 'AP, Reuters, AFP, Al Jazeera, CNN, Bloomberg, UN News, ABC, IEA and others (research.md)'
