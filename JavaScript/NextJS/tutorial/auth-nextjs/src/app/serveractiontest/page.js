import { deletePost, addPost } from "../../../lib/action";

const ServerActionTestPage = () => {

    const actionInComponent = async () => {
        "use server"
        console.log('it is working!');
    }

    return (
        <div>
            <form action={addPost}>
                <input type="text" name="title" placeholder="Title"></input>
                <input type="text" name="desc" placeholder="Description"></input>
                <input type="text" name="img" placeholder="Image url"></input>
                <input type="text" name="id" placeholder="Post ID"></input>
                <input type="text" name="userId" placeholder="User ID"></input>
                <button>Create</button>
            </form>

            <form action={deletePost}>
                <input type="text" name="id" placeholder="ID"></input>
                <button>Delete</button>
            </form>
        </div>
    )
} 

export default ServerActionTestPage