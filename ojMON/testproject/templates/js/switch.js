$('#ps1').click(function(){
	$('#ps').css({'display': 'block'});
	$('#submissions').css({'display': 'none'});
	$('#leaderboard').css({'display': 'none'});
	$('#discussions').css({'display': 'none'});
});
$('#submissions1').click(function(){
	$('#ps').css({'display': 'none'});
	$('#submissions').css({'display': 'block'});
	$('#leaderboard').css({'display': 'none'});
	$('#discussions').css({'display': 'none'});
});
$('#leaderboard1').click(function(){
	$('#ps').css({'display': 'none'});
	$('#submissions').css({'display': 'none'});
	$('#leaderboard').css({'display': 'block'});
	$('#discussions').css({'display': 'none'});
});
$('#discussions1').click(function(){
	$('#ps').css({'display': 'none'});
	$('#submissions').css({'display': 'none'});
	$('#leaderboard').css({'display': 'none'});
	$('#discussions').css({'display': 'block'});
});