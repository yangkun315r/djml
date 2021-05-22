INSERT INTO `ipb_members` (`member_id`, `name`, `member_group_id`, `email`, `joined`, `ip_address`, `posts`, `title`, `allow_admin_mails`, `time_offset`, `hide_email`, `email_full`, `skin`, `warn_level`, `warn_lastwarn`, `language`, `last_post`, `restrict_post`, `view_sigs`, `view_img`, `view_avs`, `bday_day`, `bday_month`, `bday_year`, `msg_count_new`, `msg_count_total`, `msg_count_reset`, `msg_show_notification`, `misc`, `last_visit`, `last_activity`, `dst_in_use`, `view_prefs`, `coppa_user`, `mod_posts`, `auto_track`, `temp_ban`, `sub_end`, `login_anonymous`, `ignored_users`, `mgroup_others`, `org_perm_id`, `member_login_key`, `member_login_key_expire`, `subs_pkg_chosen`, `has_blog`, `has_gallery`, `members_editor_choice`, `members_auto_dst`, `members_display_name`, `members_seo_name`, `members_created_remote`, `members_cache`, `members_disable_pm`, `members_l_display_name`, `members_l_username`, `failed_logins`, `failed_login_count`, `members_profile_views`, `members_pass_hash`, `members_pass_salt`, `identity_url`, `member_banned`, `member_uploader`, `members_bitoptions`, `fb_uid`, `fb_emailhash`, `fb_lastsync`, `members_day_posts`, `live_id`, `twitter_id`, `twitter_token`, `twitter_secret`, `notification_cnt`, `tc_lastsync`, `fb_session`, `fb_token`, `ips_mobile_token`, `chat_banned`) VALUES


{% for user in users %}
({{ user.zeta_id }}, '{{ user.username }}', 3, 'example-{{ user.username|slugify }}@example.com', {{ user.date_joined|date:"U" }}, '127.0.0.1', {{ user.post_count }}, 'Change me!', 1, NULL, '1', NULL, NULL, NULL, 0, 1, NULL, '0', 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, NULL, 1296087281, 1301611210, 0, '-1&-1', 0, '0', '0', '0', 0, '0&1', 'a:0:{}', '', '', '660d1403b21aae0036d88728612b5f30', 1302216010, 0, '', 0, 'std', 1, 'djm', 'djm', 0, 'a:3:{s:11:"report_temp";a:0:{}s:19:"report_last_updated";i:1296086791;s:10:"report_num";s:1:"0";}', 0, 'djm', 'djm', '', 0, 0, 'a0fe287c3dc1976ead0293548e8d13e2', 'E8tnL', '', 0, 'default', 0, 0, '', 0, '0,0', NULL, '', '', '', 0, 0, '', '', NULL, 0),
{% endfor %}
