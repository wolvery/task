CREATE FUNCTION range_calendar(@DataInicio datetime, @DataFim datetime)
RETURNS TABLE
AS
RETURN
( 
with cte(data_hora) as 
(
	select @DataInicio
	union all
	select DATEADD(hour, 1, data_hora) from cte where data_hora < @DataFim
	)  
	select data_hora from cte 
)
