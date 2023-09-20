/* add this file in jsconfig.json, in typeRoots array */
declare module "models" {
    import { Activity } from "@mail/core/web/activity_model";
    import { Attachment } from "@mail/core/common/attachment_model";
    import { CannedResponse } from "@mail/core/common/canned_response_model";
    import { ChannelMember } from "@mail/core/common/channel_member_model";
    import { Composer } from "@mail/core/common/composer_model";
    import { Follower } from "@mail/core/common/follower_model";
    import { LinkPreview } from "@mail/core/common/link_preview_model";
    import { Message } from "@mail/core/common/message_model";
    import { MessageReactions } from "@mail/core/common/message_reactions_model";
    import { Notification } from "@mail/core/common/notification_model";
    import { Persona } from "@mail/core/common/persona_model";
    import { RtcSession } from "@mail/discuss/call/common/rtc_session_model";
    import { Thread } from "@mail/core/common/thread_model";

    export interface Models {
        "Activity": Activity,
        "Attachment": Attachment,
        "CannedResponse": CannedResponse,
        "ChannelMember": ChannelMember,
        "Composer": Composer,
        "Follower": Follower,
        "LinkPreview": LinkPreview,
        "Message": Message & Partial<Message_Patch>,
        "MessageReactions": MessageReactions,
        "Notification": Notification,
        "Persona": Persona,
        "RtcSession": RtcSession,
        "Thread": Thread & Partial<Thread_Patch>,
    }

    export interface Message_Patch {
        pinnedAt: string,
    }

    export interface Thread_Patch {
        pinnedMessages: RecordSet<Models["Message"]>,
        pinnedMessagesState: "loaded"|"loading"|"error"|undefined,
    }

    import { RecordList, RecordSet } from "@mail/core/common/record";

    export interface Collection<T> {
        "List": RecordList<T>,
        "Set": RecordSet<T>,
    }
}
