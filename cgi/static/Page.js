
//显示添加项目的表单
function showAddProject(){
    $('form[name=add-project]').show();
}

//隐藏添加项目的表单
function hideAddProject(){
    $('form[name=add-project]').hide();
}

//删除任务item
function confirmDelete(item_id){
    if(confirm('确认删除该任务？')){
        window.location.href = '/del-item/'+item_id;
    }
}

//任务完成，嘎嘎！！
function finishItem(item_id){
    window.location.href = '/finish-item/'+item_id;
}

//任务返工
function unFinishItem(item_id){
    window.location.href = '/unfinish-item/'+item_id;
}
