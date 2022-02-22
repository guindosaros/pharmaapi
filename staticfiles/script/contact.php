<?php
/*
Template Name: Wedding Manager : Wedding Manager HTML templates

Variable
	$recaptchaSecret : Recaptcha Secret Key
 
	$dzName : Contact Person Name
	$dzEmail : Contact Person Email
	$dzMessage : Contact Person Message
	$dzRes : response holder
	$dzOtherField : Form other additional fields
	
	
	$dzMailSubject : Mail Subject.
	$dzMailMessage : Mail Body
	$dzMailHeader : Mail Header
	$dzEmailReceiver : Contact receiver email address
	$dzEmailFrom : Mail Form title
	$dzEmailHeader : Mail headers
*/
/* require ReCaptcha class */
require('recaptcha-master/src/autoload.php');

/* ReCaptch Secret */
$recaptchaSecret = '<!-- Put Your reCaptcha Secret Key -->';

$dzEmailTo 		= "info@exemple.com";   /* Receiver Email Address */
$dzEmailFrom    = "WeddingManager Contact";

function pr($value)
{
	echo "<pre>";
	print_r($value);
	echo "</pre>";
}

try {
    if (!empty($_POST)) {

        /* validate the ReCaptcha, if something is wrong, we throw an Exception,
			i.e. code stops executing and goes to catch() block */
        
        if (!isset($_POST['g-recaptcha-response'])) {
            $dzRes['status'] = 0;
			$dzRes['msg'] = 'ReCaptcha is not set.';
			echo json_encode($dzRes);
			exit;
        }

        /* do not forget to enter your secret key from https://www.google.com/recaptcha/admin */
        
        $recaptcha = new \ReCaptcha\ReCaptcha($recaptchaSecret, new \ReCaptcha\RequestMethod\CurlPost());
        
        /* we validate the ReCaptcha field together with the user's IP address */
        
        $response = $recaptcha->verify($_POST['g-recaptcha-response'], $_SERVER['REMOTE_ADDR']);

        if (!$response->isSuccess()) {
            $dzRes['status'] = 0;
			$dzRes['msg'] = 'ReCaptcha was not validated.';
			echo json_encode($dzRes);
			exit;
        }
        
		#### Contact Form Script ####
		$dzName = trim(strip_tags($_POST['dzName']));
		$dzEmail = trim(strip_tags($_POST['dzEmail']));
		$dzMessage = strip_tags($_POST['dzMessage']);	
		$dzRes = "";
		if (!filter_var($dzEmail, FILTER_VALIDATE_EMAIL)) 
		{
			$dzRes['status'] = 0;
			$dzRes['msg'] = 'Wrong Email Format.';
		}
		$dzMailSubject = 'WeddingManager|Contact Form: A Person want to contact';
		$dzMailMessage	= 	"
							A person want to contact you: <br><br>
							Name: $dzName<br/>
							Email: $dzEmail<br/>
							Message: $dzMessage<br/>
							";
							
		$dzOtherField = "";
		if(!empty($_POST['dzOther']))
		{
			$dzOther = $_POST['dzOther'];
			$message = "";
			foreach($dzOther as $key => $value)
			{
				$fieldName = ucfirst(str_replace('_',' ',$key));
				$fieldValue = ucfirst(str_replace('_',' ',$value));
				$dzOtherField .= $fieldName." : ".$fieldValue."<br>";
			}
		}
		$dzMailMessage .= $dzOtherField; 
							
		$dzEmailHeader  	= "MIME-Version: 1.0\r\n";
		$dzEmailHeader 		.= "Content-type: text/html; charset=iso-8859-1\r\n";
		$dzEmailHeader 		.= "From:$dzEmailFrom <$dzEmail>";
		$dzEmailHeader 		.= "Reply-To: $dzEmail\r\n"."X-Mailer: PHP/".phpversion();
		if(mail($dzEmailTo, $dzMailSubject, $dzMailMessage, $dzEmailHeader))
		{
			$dzRes['status'] = 1;
			$dzRes['msg'] = 'We have received your message successfully. Thanks for Contact.';
		}
		else
		{
			$dzRes['status'] = 0;
			$dzRes['msg'] = 'Some problem in sending mail, please try again later.';
		}
		echo json_encode($dzRes);
		exit;
		#### Contact Form Script End ####
		
	
		
	}
} catch (\Exception $e) {
    $dzRes['status'] = 0;
	$dzRes['msg'] = $e->getMessage().'Some problem in sending mail, please try again later.';
	echo json_encode($dzRes);
	exit;
}

?>