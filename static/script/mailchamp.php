<?php
/*
Template Name: Wedding Manager : Wedding Manager HTML templates

Variable
	$apiKey : Mail Champ Api
	$listID : List Id of mail champ
 
	$email : Subscription Email
	$fname, $lname, $phone, $subject : You can use these variables when you would add these in your mail champ list form.
	
	
	
*/

function pr($value)
{
	echo "<pre>";
	print_r($value);
	echo "</pre>";
}
if(isset($_POST)){
	$dzRes['status'] = 0;
	$dzRes['msg'] = '';
    /*
		You can use these variables when you would add these in your mail champ list form.
		
	  $fname = $_POST['fname'];
      $lname = $_POST['lname'];
	  $phone = $_POST['phone'];
	  $subject = $_POST['subject'];
	  
	 */
	
     $email = trim(strip_tags($_POST['dzEmail']));
	if(!empty($email) && !filter_var($email, FILTER_VALIDATE_EMAIL) === false){
        // MailChimp API credentials
        $apiKey = '<!-- Put Your Mail Champ API Key -->';
        $listID = '<!-- Put Your Mail Champ List ID -->';
        
        // MailChimp API URL
        $memberID = md5(strtolower($email));
        $dataCenter = substr($apiKey,strpos($apiKey,'-')+1);
        $url = 'https://' . $dataCenter . '.api.mailchimp.com/3.0/lists/' . $listID . '/members/' . $memberID;
        
        // member information
        $json = json_encode([
            'email_address' => $email,
			'status'        => 'subscribed'
            /*'merge_fields'  => [
                //'FNAME'     => $fname,
                //'LNAME'     => $lname,
				//'PHONE'     => $phone,
				//'SUBJECT'   => $subject,
			]*/
        ]);
        
        // send a HTTP POST request with curl
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_USERPWD, 'user:' . $apiKey);
        curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 10);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
        $result = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        
		// store the status message based on response code
        if ($httpCode == 200) {
			$dzRes['status'] = 1;
            $dzRes['msg'] = 'You have successfully subscribed.';
        } else {
            switch ($httpCode) {
                case 214:
                    $msg = 'You are already subscribed.';
                    break;
                default:
                    $msg = 'Some problem occurred, please try again.';
                    break;
            }
            $dzRes['msg'] = $msg;
        }
    }else{
        $dzRes['msg'] = 'Please enter valid email address.';
    }
	echo json_encode($dzRes);
	exit;
}
