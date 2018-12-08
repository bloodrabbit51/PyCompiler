/*******************************************************************************
**                      KPIT Technologies Limited                             **
**                                                                            **
** KPIT Technologies Limited owns all the rights to this work. This work      **
** shall not be copied, reproduced, used, modified or its information         **
** disclosed without the prior written authorization of KPIT Technologies     **
** Limited.                                                                   **
**                                                                            **
**  SRC-MODULE: App_BswM_Common_TCs.c                                         **
**                                                                            **
**  TARGET    : All                                                           **
**                                                                            **
**  PRODUCT   : AUTOSAR BSWM                                                  **
**                                                                            **
**  PURPOSE   : This application file is used to test the Functionality of    **
**              Communication request from CanSM,ComM and Dcm to BswM.        **
**                                                                            **
**                                                                            **
**  PLATFORM DEPENDANT [yes/no]: no                                           **
**                                                                            **
**  TO BE CHANGED BY USER [yes/no]: no                                        **
**                                                                            **
*******************************************************************************/
/*******************************************************************************
**                      Revision History                                      **
********************************************************************************
** Revision     Date     Changed By         Description                       **
********************************************************************************
** 1.0.0     07-Sept-2015   Srujana K        Initial version                  **
*******************************************************************************/
/*******************************************************************************
**                     Include Section                                        **
*******************************************************************************/
#include "App_BswM_Common_TCs.h"
#include "BswM.h"
#include "EcuM.h"
#include "J1939Dcm.h"
#include "J1939Rm.h"
#include "Sd.h"
#include "CanNm.h"
#include "ComM.h"
#include "PduR.h"
#include "SchM_BswM.h"
#include "Rte_BswM.h"
#include "BswM_Ram.h"
#include "Com.h"
#include "Nm.h"
#include "BswM_ComM.h"
#include "BswM_CanSM.h"
#include "BswM_LinSM.h"
#include "BswM_FrSM.h"
#include "BswM_EthSM.h"
#include "BswM_EcuM.h"
#include "Det.h"
#include "BswM_NvM.h"
/*******************************************************************************
**                      Macros                                                **
*******************************************************************************/

/*******************************************************************************
**                      Global Data Types                                     **
*******************************************************************************/

/*******************************************************************************
**                      Function Prototypes                                   **
*******************************************************************************/

/*******************************************************************************
**                            XTESTCASEXID                                    **
*******************************************************************************/
uint8 XTESTCASEXID (void)