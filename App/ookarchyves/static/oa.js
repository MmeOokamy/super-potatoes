$(document).ready(function(){
        $(".oa_article").on("click", function(){
            let id = $(this).data('article');
            let url = $(this).data('url');
            if(id){
                $.ajax({
                    type: 'GET',
                    url: url,
                    data: 'id='+id,
                    success: function(data){
                        console.log(data['art_obj']);
                        let a = data['art_obj'];
                        $("#article-title").html(a.title)
                        $("#article-body").html(a.body)
                        $("#article-trash").attr('data-article-id', a.id)
                        
                    }

                });
            };
        });

        $("#article-trash").on("click", function(){
            let id = $(this).data('article-id');
            let url = $(this).data('url');
            if(id){
                $.ajax({
                    type: 'GET',
                    url: url,
                    data: 'id='+id,
                    success: function(data){
                        // console.log(data);
                        if (data['response'] === "D"){
                            // M.toast({html: 'I am a toast!'})
                            location.reload();
                        } else {
                            alert(data['response'])
                        }
                    }
                });
            };
        })
})