function goodbye() {
  text = $('#hello').text();
  if (text.indexOf('Hello') == 0)
    {
       $('#hello').html("Goodbye cruel world!");    
      $('#mybutton').text("Say Hello!");    
    }
  else
    {
      $('#hello').html("Hello World!");    
      $('#mybutton').text("Say Goodbye");    
    }
  
}
