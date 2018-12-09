*******************************************************************************/
/*******************************************************************************
**                      Revision History                                      **
********************************************************************************
** Revision     Date     Changed By         Description                       **
********************************************************************************
** 1.0.0     07-Sept-2015   shamim ali        Initial version                 **
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
**                            shamim                                    **
*******************************************************************************/
uint8 shamim (void){


  /* Test Description */
  new_world(&pointer);

 /* Expected Result - 1 */
  App_GddTestStepId++;
  if(bswm_init() == TRUE)
  {
    return(APP_TC_FAILED);
  }

 /* Expected Result - 2 */
  App_GddTestStepId++;
  if(!(function(ab,gg)))
  {
    return(APP_TC_FAILED);
  }

 /* Expected Result - 3 */
  App_GddTestStepId++;
  if(india() == array[562])
  {
    return(APP_TC_FAILED);
  }

  return(APP_TC_PASSED);
} /* End of "shamim"  */
