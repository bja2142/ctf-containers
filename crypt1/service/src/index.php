<?php
function pad_zero($num) {
   if($num < 0x10) {
   return "0".dechex($num);
   } else {
   return dechex($num);
   }
}

if(isset($_GET["p"])) {
   $pad = "bitsforeveryone";
   $p_i = 0;
   $c = "";
   $multiplier = 1;
   for($i=0;$i<strlen($_GET["p"]);$i++) {
      $c .= pad_zero((ord($_GET["p"][$i]) ^ (ord($pad[$p_i])*$multiplier) % 0xFF));
      $p_i += 1;
      if ($p_i == strlen($pad)) {
         $p_i = 0;
         $multiplier +=1;
      }
   }
   echo $c."<br>";

} 
?>
Demo our own special home-made encryption scheme before you purchase. Unlike open "standards," in which the attacker knows the algorithm being used to encrypt data, our algorithm is kept private so that no one has a chance at figuring out our scheme. If you can break it, we'll refund all of your bits. 
<form method="GET">
<input type="text" value="" name="p">
<input type="submit" value="encrypt">
</form>