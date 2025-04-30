| Column Name                    | Description                                                      | Example          |
| ------------------------------ | ---------------------------------------------------------------- | ---------------- |
| typeCode                       | Type of trade data (e.g., "C" for commodities)                   | C                |
| freqCode                       | Data frequency: A = Annual, M = Monthly                          | A                |
| refPeriodId                    | Reference period in YYYYMMDD format                              | 20080101         |
| refYear                        | Trade year                                                       | 2008             |
| refMonth                       | Trade month (if monthly data; otherwise unused)                  | 1, 12            |
| period                         | Redundant year field (same as refYear)                           | 2008             |
| reporterCode                   | Numerical code for reporting country                             | 36               |
| reporterISO                    | ISO3 country code of reporting country                           | AUS              |
| reporterDesc                   | Full name of reporting country                                   | Australia        |
| flowCode                       | Trade flow: Import or Export                                     | Import           |
| flowDesc                       | Redundant or numerical description of trade flow                 | 1, 2             |
| partnerCode                    | Numerical code for partner (trade counterpart) country           | 124              |
| partnerISO                     | ISO3 code of trade partner country                               | CAN              |
| partnerDesc                    | Full name of trade partner                                       | Canada           |
| partner2Code                   | Secondary partner (used in complex trade scenarios)              | may be null      |
| classificationCode             | Classification system used (e.g., HS 2012, SITC)                 | HS               |
| cmdCode                        | Commodity code based on classification                           | 1001             |
| cmdDesc                        | Description of the commodity                                     | Wheat            |
| aggrLevel                      | Boolean flag if this is an aggregated product category           | True/False       |
| isLeaf                         | True if the commodity is the most detailed level in hierarchy    | True/False       |
| customsCode                    | Customs procedure code (optional, depending on country)          | varies           |
| customsDesc                    | Description of customs procedure                                 | varies           |
| mosCode, motCode               | Mode of supply / mode of transport codes (optional)              | 1, 5             |
| qtyUnitCode, qtyUnitAbbr       | Code and abbreviation for the quantity unit                      | 8, kg            |
| qty                            | Reported trade quantity                                          | 120000           |
| isQtyEstimated                 | Flag indicating if the quantity value was estimated              | 0 (no), 1 (yes)  |
| altQtyUnitCode, altQtyUnitAbbr | Alternate quantity units (if available)                          | No data          |
| altQty                         | Value in alternate units                                         | may be null      |
| isAltQtyEstimated              | Flag for estimated alternate quantity                            | 1 or 0           |
| netWgt                         | Net weight in kilograms                                          | 5000             |
| isNetWgtEstimated              | Whether the net weight was estimated                             | True/False       |
| grossWgt                       | Gross weight in kilograms                                        | may be null      |
| isGrossWgtEstimated            | Whether gross weight was estimated                               | True/False       |
| cifvalue                       | Cost, Insurance, and Freight value (value at import destination) | 1.2e+09          |
| fobvalue                       | Free on Board value (value at export origin)                     | 1.0e+09          |
| primaryValue                   | Indicates which value (FOB or CIF) is the primary one            | 0 or 4           |
| legacyEstimationFlag           | Historical estimation method flag                                | True/False       |
| isReported                     | Whether the data was reported directly or imputed                | True/False       |
| isAggregate                    | Whether this row is an aggregate entry                           | was 100% missing |
