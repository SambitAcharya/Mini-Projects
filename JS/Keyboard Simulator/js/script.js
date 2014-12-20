$(function(){
    
    var $write = $('#write'),
        shift = false,
        capslock = false;

        $('#keyboard li').click(function(){
            var $this = $(this),
                character = $this.html();
        

        // Shift
        
        if($this.hasClass('left-shift') || $this.hasClass('right-shift')){
            $('.letter').toggleClass('uppercase');
            $('.symbol span').toggle();

            shift = (shift === true) ? false: true;
            capslock = false;
            return false;
        }

        // Caps Lock
        
        if($this.hasClass('capslock')){
            $('.letter').toggleClass('uppercase');
            capslock = true;
            return false;
        }

        // Delete
        
        if ($this.hasClass('delete')){
            var html = $write.html();

            $write.html(html.substr(0,html.length - 1));
            return false;
        }

        // Special Characters
        
        if ($this.hasClass('symbol'))
            character = $('span:visible', $this).html();
        
        if ($this.hasClass('space'))
            character = ' ';
        
        if($this.hasClass('tab'))
            character = "\t";
        
        if($this.hasClass('return'))
            character = "\n";

        // Uppercase Letters
        
        if($this.hasClass('uppercase'))
              character = character.toUpperCase();

        // Remove shift once a key is clicked
         
        if (shift === true){
            $('.symbol span').toggle();
            if (capslock === false)
                $('.letter').toggleClass('uppercase');

            shift = false;
        }

        $write.html($write.html() + character);
    });
});