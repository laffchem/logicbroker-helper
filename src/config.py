queries = {
    "hold": """UPDATE `logicbroker-fulfillment`.order
SET status = 'hold'
WHERE AgreementId IN (
    {data}
)
AND status = 'signed';""",
    "release": """UPDATE `logicbroker-fulfillment`.order
SET status = 'signed'
WHERE AgreementId IN (
    {data}
)
AND status = 'hold';""",
    "view": """SELECT *
FROM `logicbroker-fulfillment`.order where isTest=0
and AgreementId IN (
    {data}
)
;""",
    "bb_release": """UPDATE `logicbroker-fulfillment`.order
SET DateToSubmitPo = NOW()
WHERE VendorId = '58b24308bb25690011a6a49a'
AND AgreementId IN (
    {data}
)
; """,
    "repeat_customer_release": """UPDATE `logicbroker-fulfillment`.order
SET DateToSubmitPo = NOW()
WHERE AgreementId IN (
    {data}
) and status = 'signed'
; """,
}
