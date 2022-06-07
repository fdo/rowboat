echo select * from todo_running where rowid = %1; >  templook
echo select * from todo_running where rowid = %2; >> templook
echo select * from todo_running where rowid = %3; >> templook
echo select * from todo_weight  where rowid = %4; >> templook
echo select * from todo_weight  where rowid = %5; >> templook
echo select * from todo_weight  where rowid = %6; >> templook
type templook
