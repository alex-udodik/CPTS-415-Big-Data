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
    Name VARCHAR(255),
    Buy INTEGER,
    Catalog VARCHAR(255),
    Source VARCHAR(255),
    Filename VARCHAR(255),
    Version VARCHAR(255),
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE DressUp (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255), /* Might need to be changed */
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    PrimaryShape VARCHAR(255),
    SecondaryShape VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Fencing (
    Name VARCHAR(255),
    DIY BOOLEAN,
    StackSize INTEGER,
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Fish (
    Number INTEGER UNIQUE,
    Name VARCHAR(255),
    Sell INTEGER,
    Where VARCHAR(255),
    Shadow VARCHAR(255),
    TotalCatchesToUnlock INTEGER,
    SpawnRates VARCHAR(255), /* Might need to be changed */
    RainSnow BOOLEAN,

    NHJan VARCHAR(255), /* Might need to be changed */
    NHFeb VARCHAR(255), /* Might need to be changed */
    NHMar VARCHAR(255), /* Might need to be changed */
    NHApr VARCHAR(255), /* Might need to be changed */
    NHMay VARCHAR(255), /* Might need to be changed */
    NHJun VARCHAR(255), /* Might need to be changed */
    NHJul VARCHAR(255), /* Might need to be changed */
    NHAug VARCHAR(255), /* Might need to be changed */
    NHSep VARCHAR(255), /* Might need to be changed */
    NHOct VARCHAR(255), /* Might need to be changed */
    NHNov VARCHAR(255), /* Might need to be changed */
    NHDec VARCHAR(255), /* Might need to be changed */

    SHJan VARCHAR(255), /* Might need to be changed */
    SHFeb VARCHAR(255), /* Might need to be changed */
    SHMar VARCHAR(255), /* Might need to be changed */
    SHApr VARCHAR(255), /* Might need to be changed */
    SHMay VARCHAR(255), /* Might need to be changed */
    SHJun VARCHAR(255), /* Might need to be changed */
    SHJul VARCHAR(255), /* Might need to be changed */
    SHAug VARCHAR(255), /* Might need to be changed */
    SHSep VARCHAR(255), /* Might need to be changed */
    SHOct VARCHAR(255), /* Might need to be changed */
    SHNov VARCHAR(255), /* Might need to be changed */
    SHDec VARCHAR(255), /* Might need to be changed */

    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    LightingType VARCHAR(255),
    IconFileName VARCHAR(255),
    CritterpediaFilename VARCHAR(255),
    Furniture VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Floors (
    Name VARCHAR(255),
    VFX BOOLEAN,
    DIY BOOLEAN,
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    HHAConcept1 VARCHAR(255),
    HHAConcept2 VARCHAR(255),
    HHASeries VARCHAR(255),
    Tag VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Fossils (
    Name VARCHAR(255),
    Buy VARCHAR(255),
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    Museum VARCHAR(255),
    Version VARCHAR(255),
    Interact BOOLEAN,
    Catalog VARCHAR(255), /* Might need to be changed*/
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Headwear (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    MilesPrice VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255), /* Might need to be changed */
    Type VARCHAR(255),
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Housewares (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    BodyTitle VARCHAR(255),
    Pattern VARCHAR(255),
    PatternTitle VARCHAR(255),
    DIY BOOLEAN,
    BodyCustomize BOOLEAN,
    PatternCustomize BOOLEAN,
    KitCost VARCHAR(255), /* Might need to be changed */
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    HHAConcept1 VARCHAR(255),
    HHAConcept2 VARCHAR(255),
    HHASeries VARCHAR(255),
    HHASet VARCHAR(255),
    Interact BOOLEAN,
    Tag VARCHAR(255),
    Outdoor BOOLEAN,
    SpeakerType VARCHAR(255),
    LightingType VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    VariantID VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Insects (
    Number INTEGER,
    Name VARCHAR(255),
    Sell INTEGER,
    Where VARCHAR(255),
    Weather VARCHAR(255),
    TotalCatchesToUnlock INTEGER,
    SpawnRates INTEGER,

    NHJan VARCHAR(255), /* Might need to be changed */
    NHFeb VARCHAR(255), /* Might need to be changed */
    NHMar VARCHAR(255), /* Might need to be changed */
    NHApr VARCHAR(255), /* Might need to be changed */
    NHMay VARCHAR(255), /* Might need to be changed */
    NHJun VARCHAR(255), /* Might need to be changed */
    NHJul VARCHAR(255), /* Might need to be changed */
    NHAug VARCHAR(255), /* Might need to be changed */
    NHSep VARCHAR(255), /* Might need to be changed */
    NHOct VARCHAR(255), /* Might need to be changed */
    NHNov VARCHAR(255), /* Might need to be changed */
    NHDec VARCHAR(255), /* Might need to be changed */

    SHJan VARCHAR(255), /* Might need to be changed */
    SHFeb VARCHAR(255), /* Might need to be changed */
    SHMar VARCHAR(255), /* Might need to be changed */
    SHApr VARCHAR(255), /* Might need to be changed */
    SHMay VARCHAR(255), /* Might need to be changed */
    SHJun VARCHAR(255), /* Might need to be changed */
    SHJul VARCHAR(255), /* Might need to be changed */
    SHAug VARCHAR(255), /* Might need to be changed */
    SHSep VARCHAR(255), /* Might need to be changed */
    SHOct VARCHAR(255), /* Might need to be changed */
    SHNov VARCHAR(255), /* Might need to be changed */
    SHDec VARCHAR(255), /* Might need to be changed */

    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    IconFileName VARCHAR(255),
    CritterpediaFilename VARCHAR(255),
    Furniture VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Miscellaneous (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    BodyTitle VARCHAR(255),
    Pattern VARCHAR(255),
    PatternTitle VARCHAR(255),
    DIY BOOLEAN,
    BodyCustomize BOOLEAN,
    PatternCustomize BOOLEAN,
    KitCost VARCHAR(255), /* Might need to be changed */
    Buy VARCHAR(255), /* Might need to be changed*/
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    HHAConcept1 VARCHAR(255),
    HHAConcept2 VARCHAR(255),
    HHASeries VARCHAR(255),
    HHASet VARCHAR(255),
    Interact BOOLEAN,
    Tag VARCHAR(255),
    Outdoor BOOLEAN,
    SpeakerType VARCHAR(255),
    LightingType VARCHAR(255),
    Filename VARCHAR(255),
    VariantID VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Music (
    Name VARCHAR(255),
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Other (
    Name VARCHAR(255),
    DIY BOOLEAN,
    StackSize INTEGER,
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Tag VARCHAR(255),
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Version VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Photos (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    BodyTitle VARCHAR(255),
    Pattern VARCHAR(255),
    PatternTitle VARCHAR(255),
    DIY BOOLEAN,
    Customize BOOLEAN,
    KitCost INTEGER,
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    VariantID VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE

);

CREATE TABLE Posters (
    Name VARCHAR(255),
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Reactions (
    Name VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Recipes (
    Name VARCHAR(255),
    Number1 INTEGER,
    Material1 VARCHAR(255),
    Number2 INTEGER,
    Material2 VARCHAR(255),
    Number3 INTEGER,
    Material3 VARCHAR(255),
    Number4 INTEGER,
    Material4 VARCHAR(255),
    Number5 INTEGER,
    Material5 VARCHAR(255),
    Number6 INTEGER,
    Material6 VARCHAR(255),
    Buy VARCHAR(255), /* Might need to be changed */
    Sell INTEGER,
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    NumberOfRecipesToUnlock INTEGER,
    Version VARCHAR(255),
    Category VARCHAR(255),
    SerialID INTEGER,
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Rugs (
    Name VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    HHAConcept1 VARCHAR(255),
    HHAConcept2 VARCHAR(255),
    HHASeries VARCHAR(255),
    Tag VARCHAR(255),
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Shoes (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255), /* Might need to be changed */
    MilesPrice VARCHAR(255), /* Might need to be changed */
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255), /* Might beed to be changed */
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Socks (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    MilesPrice VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255),
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Tools (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    BodyTitle VARCHAR(255),
    DIY BOOLEAN,
    Customize BOOLEAN,
    KitCost VARCHAR(255),
    Uses VARCHAR(255),
    StackSize INTEGER,
    Buy VARCHAR(255), 
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    Set VARCHAR(255),
    MilesPrice VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    Filename VARCHAR(255),
    VariantID VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Tops (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    DIY BOOLEAN,
    Buy INTEGER,
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    MilesPrice VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    SeasonalAvailability VARCHAR(255),
    MannequinPiece BOOLEAN,
    Version VARCHAR(255),
    Style VARCHAR(255),
    LabelThemes VARCHAR(255), /* Might need to be changed */
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Umbrellas (
    Name VARCHAR(255),
    DIY BOOLEAN,
    Buy VARCHAR(255),
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    MilesPrice VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    VillagerEquippable BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Villagers (
    Name VARCHAR(255),
    Species VARCHAR(255),
    Gender VARCHAR(255),
    Personality VARCHAR(255),
    Hobby VARCHAR(255),
    Birthday VARCHAR(255),
    Catchphrase VARCHAR(255),
    FavoriteSong VARCHAR(255),
    Style1 VARCHAR(255),
    Style2 VARCHAR(255),
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Wallpaper VARCHAR(255),
    Flooring VARCHAR(255),
    FurnitureList VARCHAR(255), /*Might need to be changed*/
    Filename VARCHAR(255),
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE WallMounted (
    Name VARCHAR(255),
    Variation VARCHAR(255),
    BodyTitle VARCHAR(255),
    Pattern VARCHAR(255),
    PatternTitle VARCHAR(255),
    DIY BOOLEAN,
    BodyCustomize BOOLEAN,
    PatternCustomize BOOLEAN,
    KitCost VARCHAR(255),
    buy VARCHAR(255),
    Sell INTEGER,
    Color1 VARCHAR(255),
    Color2 VARCHAR(255),
    Size VARCHAR(255),
    Source VARCHAR(255),
    SourceNotes VARCHAR(255),
    Version VARCHAR(255),
    HHAConcept1 VARCHAR(255),
    HHAConcept2 VARCHAR(255),
    HHASeries VARCHAR(255),
    HHASet VARCHAR(255),
    Interact BOOLEAN,
    Tag VARCHAR(255),
    Outdoor BOOLEAN,
    LightingType VARCHAR(255),
    DoorDeco BOOLEAN,
    Catalog VARCHAR(255),
    Filename VARCHAR(255),
    VariantID VARCHAR(255),
    InternalID INTEGER,
    UniqueEntryID VARCHAR(255) UNIQUE
);

CREATE TABLE Wallpaper (

);