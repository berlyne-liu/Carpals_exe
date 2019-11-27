select tempa.ERBS,tempa.CELL,tempa.Type,tempa.Scene,tempx.state,tempy.alarmObject
from
(select * from
(select ERBS,CELL,
case  
when substr(ERBS,-3,3) in ("ELH","ELW","ELR")THEN "TDD"																										 
when substr(ERBS,-3,3) in ("EFH","EFW","EFR") THEN "FDD"
else "TDD"
end as "Type"
from Config_CellsList) as tempA
left join
(select "小区" as CELL,GROUP_CONCAT("覆盖场景") AS Scene from Config_SceneList
group by "小区"
) as ScenList
ON ScenList.CELL=tempa.CELL) as tempa
left join
(select tempa.NodeId,tempa.EUtranCellFDDId,
case
WHEN (tempb.synstatus<>"DROPLINE" AND tempa.ad_state="LOCKED") THEN "闭塞"
WHEN (tempb.synstatus<>"DROPLINE" and tempa.ad_state="DISABLED") THEN "退服"
WHEN tempb.synstatus="DROPLINE" THEN "脱管"
ELSE "正常"
END AS "state"
from
(select NodeId,EUtranCellFDDId,
CASE
WHEN administrativeState="LOCKED" THEN "LOCKED"
WHEN administrativeState="UNLOCKED" THEN operationalState
END AS ad_state
from Alarm_State) as tempa
left join
(select NodeId,
case 
WHEN syncStatus="UNSYNCHRONIZED" THEN "DROPLINE"
else syncStatus
END AS synstatus
from Alarm_syncStatus) as tempb
ON tempb.NodeId=tempa.NodeId
) as tempx
on tempx.EUtranCellFDDId = tempa.CELL
left join
(select Nodeid,GROUP_CONCAT(alarm," | ") as "alarmObject"
from
(select Nodeid,STRFTIME('%Y-%m-%d %H:%M:%S', "dateid","localtime")||"  "||c."告警解析"||"("||"Alarmobject"||")" as "alarm"
from
(select * from
(
select replace("Network Element","NetworkElement=","") AS "Nodeid",
substr("Event Time",-4,4)||"-"||
case 
when substr("Event Time",5,3)="Jan" then "01"
when substr("Event Time",5,3)="Feb" then "02"
when substr("Event Time",5,3)="Mar" then "03"
when substr("Event Time",5,3)="Apr" then "04"
when substr("Event Time",5,3)="May" then "05"
when substr("Event Time",5,3)="Jun" then "06"
when substr("Event Time",5,3)="Jul" then "07"
when substr("Event Time",5,3)="Aug" then "08"
when substr("Event Time",5,3)="Sep" then "09"
when substr("Event Time",5,3)="Oct" then "10"
when substr("Event Time",5,3)="Nov" then "11"
when substr("Event Time",5,3)="Dec" then "12"
END ||"-"||
substr("Event Time",-20,2)||
substr("Event Time",-8,-10) as "dateid",
"Specific Problem",
replace("Alarming Object","EUtranCellFDD=","") as "Alarmobject"
from Alarm_Cause
) as a
LEFT JOIN
(select "告警标题","告警解析" from Config_AlarmList) as b
on a."Specific Problem"=b."告警标题"
where b."告警标题" is not null
) as c
) as d
GROUP BY Nodeid
) as tempy
on tempy.Nodeid=tempx.NodeId