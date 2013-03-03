
//显示添加项目的表单
function showAddProject(){
    $('form[name=add-project]').show();
}

//隐藏添加项目的表单
function hideAddProject(){
    $('form[name=add-project]').hide();
}

//删除项目Project
function confirmDeleteProject(project_id){
    if(confirm('确认删除该项目？')){
        window.location.href = '/del-project/'+project_id;
    }
}

//编辑项目Project
function editProject(this_project, project_id){
    dd = $(this_project).parent();
    $('.update_project').hide();
    $('.project_title').show();
    dd.children('.project_title, .edit_project, .del_project').hide();
    dd.children('.update_project').show();
    dd.children('.update_project').children('input.title').focus().keyup(function(){
        if(event.keyCode==13){
            $(this).parent().submit();
        }
    });


}

//删除任务item
function confirmDeleteItem(item_id){
    if(confirm('确认删除该任务？')){
        window.location.href = '/del-item/'+item_id;
    }
}

//编辑任务item
function editItem(this_item, item_id){
    dd = $(this_item).parent();
    $('.update_item').hide();
    $('.item_content, .checker').show();
    dd.children('.item_content, .checker, .edit_item, .del_item').hide();
    dd.children('.update_item').show();
    dd.children('.update_item').children('input.content').focus().keyup(function(){
        if(event.keyCode==13){
            $(this).parent().submit();
        }
    });


}

//任务完成
function finishItem(item_id){
    window.location.href = '/finish-item/'+item_id;
}

//任务返工
function unFinishItem(item_id){
    window.location.href = '/unfinish-item/'+item_id;
}
