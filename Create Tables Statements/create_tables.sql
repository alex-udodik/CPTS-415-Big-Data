CREATE TABLE Accessories (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    UniqueValue VARCHAR(255), /* Might need to be changed */
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255),
    Type VARCHAR(255),
    VillagerEquippable BOOLEAN,
    Catelog BOOLEAN, /* Might need to be changed */
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Achievements (
    Name VARCHAR(255) UNIQUE,
    AwardCriteria VARCHAR(255), 
    Number INTEGER,
    InternalID INTEGER,
    InternalName VARCHAR(255),
    InternalCategory VARCHAR(255),
    NumOfTiers INTEGER,
    Tier1 INTEGER,
    Tier2 INTEGER,
    Tier3 INTEGER,
    Tier4 INTEGER,
    Tier5 INTEGER,
    RewardTier1 INTEGER,
    RewardTier2 INTEGER,
    RewardTier3 INTEGER,
    RewardTier4 INTEGER,
    RewardTier5 INTEGER,
    RewardTier6 INTEGER,
    Sequential BOOLEAN,
    Version VARCHAR(255),
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Art (
    Name VARCHAR(255),
    Genuine BOOLEAN,
    Category VARCHAR(255),
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed*/
    RealArtworkTitle VARCHAR(255),
    Artist VARCHAR(255),
    MuseumDescription VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    HHAConcept1 VARCHAR(255),
    HHAConcept2 VARCHAR(255),
    HHASeries VARCHAR(255),
    HHASet VARCHAR(255),
    Interact BOOLEAN,
    Tag VARCHAR(255),
    SpeakerType VARCHAR(255),
    LightingType VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Bags (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy VARCHAR,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    MilesPrice VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255),
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255)
);

CREATE TABLE Bottoms (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255), /* Might need to be changed*/
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER, 
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Construction (

);

CREATE TABLE DressUp (

);

CREATE TABLE Fencing (

);

CREATE TABLE Fish (

);

CREATE TABLE Floors (

);

CREATE TABLE Fossils (

);

CREATE TABLE Headwear (

);

CREATE TABLE Housewares (

);

CREATE TABLE Insects (

);

CREATE TABLE Miscellaneous (

);

CREATE TABLE Music (

);

CREATE TABLE Other (

);

CREATE TABLE Photos (

);

CREATE TABLE Posters (

);

CREATE TABLE Reactions (

);

CREATE TABLE Recipes (

);

CREATE TABLE Rugs (

);

CREATE TABLE Shoes (

);

CREATE TABLE Socks (

);

CREATE TABLE Tools (

);

CREATE TABLE Tops (

);

CREATE TABLE Umbreallas (

);

CREATE TABLE Villagers (

);

CREATE TABLE WallMounted (

);

CREATE TABLE Wallpaper (

);