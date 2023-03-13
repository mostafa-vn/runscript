<?php
if (isset($_REQUEST['q']) && isset($_REQUEST['i'])){
	$input = $_REQUEST['i'];
	$type = $_REQUEST['q'];
	$db = new mysqli('localhost','license_license','JB43JgFJRE0m','license_license');
	$db->set_charset('utf8');
	switch ($type) {
		case '0':
		// SAVE USER INFO WHEN USES UNLICENSD THEME 
		//SAMPLE OUTPUT : Array ( [ip] => 127.0.0.1 [ua] => Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0 [time] => 1584625272 [httpHost] => 127.0.0.1 [serverName] => 127.0.0.1 [serverAddr] => 127.0.0.1 ) 
		$UnlicensedUserInfo = (unserialize(base64_decode(urldecode($input))));
		$i=0;
		$values="";
		foreach ($UnlicensedUserInfo as $key => $value) {
			if($i==0){
				$values .= "null,'$value',";
			}else if($i+1 == count($UnlicensedUserInfo)){
				$values .= "'$value'";
			}else{
				$values .= "'$value',";
			}
			$i++;
		}
		$db->query("INSERT INTO unlicensedUsersInfo VALUES($values);");
			break;
		case '1':
		//Domain only
		$allowedDarr=$db->query("SELECT * FROM allowedDomains");
		$allowedDomains= array();
		while ($domain = $allowedDarr->fetch_assoc()) {
			$allowedDomains[] = $domain['domain'];
		}
		if(in_array($input, $allowedDomains)){
			echo md5(base64_encode(md5($input)));
		}
			break;
		default:
			break;
	}
}
?>