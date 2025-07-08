# Card Company
    CardCompany:
        Visa. [property Visa]
        MasterCard. [property MasterCard]
        AmericanExpress. [property AmericanExpress]
# Characters
    Presence of Non-Numeric Characters:
        None.
        Some.
# Length
    Length:
        0. [property empty]
        1.
        15. [if AmericanExpress]
        16. [if Visa || MasterCard]
        17.
# Checksum
    ValidChecksum:
        Yes. [if !empty]
        No. [if !empty]
# Prefix
    Prefix: 
        4. [if !empty && Visa]
        3.
        5.
        51-55,2221-2720. [if !empty && MasterCard]
        50.
        56.
        2220.
        2721.
        34,37. [if !empty && AmericanExpress]
        33.
        35.
        36.
        38.
