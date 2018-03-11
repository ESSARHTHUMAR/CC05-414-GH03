<script type="text/javascript">
var abc= 'this is text';
<?php $abc = "<script>document.write(abc)</script>"?>   
</script>
<?php echo $abc;?>