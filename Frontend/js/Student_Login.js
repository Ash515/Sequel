const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
var ck_email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i
function Validate(mail,password) 
{
  var email = form.email.value;
  var password = form.password.value;
  var errors = [];

   if (!ck_email.test(email)) {
    errors[errors.length] = "You must enter a valid email address.";
   }

   if (password=='') {
    errors[errors.length] = "You must enter the password ";
   }

   if (errors.length > 0) {        
    reportErrors(errors);
    return false;
   }
    return true;
  }

 function reportErrors(errors){
   var msg = "Please Enter Valide Data...\n";
   for (var i = 0; i<errors.length; i++) {
   var numError = i + 1;
    msg += "\n" + numError + ". " + errors[i];
  }
   alert(msg);
}