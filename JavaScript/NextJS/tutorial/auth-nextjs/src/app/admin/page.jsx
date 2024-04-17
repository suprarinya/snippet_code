import { Suspense } from "react";
import styles from "./admin.module.css"
import { auth } from "../../../lib/auth";
import AdminPostForm from "@/components/adminPostForm/adminPostForm";
import AdminPosts from "@/components/adminPosts/adminPosts";
import AdminUsers from "@/components/adminUsers/adminUsers";
import AdminUserForm from "@/components/adminUsersForm/adminUsersForm";

const AdminPage = async () => {
    const session = await auth()

    return (
        <div className={styles.container}>
            <div className={styles.row}>
                <div className={styles.col}>
                    <Suspense fallback={<div>Loading...</div>}>
                        < AdminPosts/>
                    </Suspense>
                </div>
                <div className={styles.col}>
                    < AdminPostForm/>
                </div>
            </div>
            <div className={styles.row}>
                <div className={styles.col}>
                    <Suspense fallback={<div>Loading...</div>}>
                        < AdminUsers/>
                    </Suspense>
                </div>
                <div className={styles.col}>
                    < AdminUserForm/>
                </div>
            </div>
        </div>
    )
}

export default AdminPage;